from django.shortcuts import render, redirect, get_object_or_404
from . models import Alumno, Curso, Matricula

# Alumnos
def inicio(request):
    return render(request, 'frontend_appescuela/base.html')

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'frontend_appescuela/ver_alumno.html', {'alumnos': alumnos})

def detalle_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'frontend_appescuela/detalles_alumno.html', {'alumno': alumno})

def crear_alumno(request):
    if request.method == 'POST':
        ap = request.POST.get('ApellidoPaterno')
        am = request.POST.get('ApellidoMaterno')
        nombres = request.POST.get('Nombres')
        num_control = request.POST.get('NumControl')
        fecha_nac = request.POST.get('FechaNacimiento')
        sexo = request.POST.get('Sexo')
        foto = request.FILES.get('foto_alumno')  # 👈 Recibir archivo de imagen
        Alumno.objects.create(
            ApellidoPaterno=ap,
            ApellidoMaterno=am,
            Nombres=nombres,
            NumControl=num_control,
            FechaNacimiento=fecha_nac,
            Sexo=sexo,
            foto_alumno=foto  # 👈 Guardar la foto
        )
        return redirect('frontend_appescuela:ver_alumnos')
    return render(request, 'frontend_appescuela/crear_alumno.html')

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.ApellidoPaterno = request.POST.get('ApellidoPaterno')
        alumno.ApellidoMaterno = request.POST.get('ApellidoMaterno')
        alumno.Nombres = request.POST.get('Nombres')
        alumno.NumControl = request.POST.get('NumControl')
        alumno.FechaNacimiento = request.POST.get('FechaNacimiento')
        alumno.Sexo = request.POST.get('Sexo')
        # Actualizar foto solo si se selecciona una nueva
        nueva_foto = request.FILES.get('foto_alumno')
        if nueva_foto:
            alumno.foto_alumno = nueva_foto  # 👈 Se reemplaza la foto
        alumno.save()
        return redirect('frontend_appescuela:ver_alumnos')
    return render(request, 'frontend_appescuela/editar_alumno.html', {'alumno': alumno})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('frontend_appescuela:ver_alumnos')
    return render(request, 'frontend_appescuela/eliminar_alumno.html', {'alumno': alumno})

# Cursos
def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'frontend_appescuela/ver_curso.html', {'cursos': cursos})

def detalle_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'frontend_appescuela/detalle_curso.html', {'curso': curso})

def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('Nombre')
        creditos = request.POST.get('Creditos')
        estado = request.POST.get('Estado') == 'on'
        foto = request.FILES.get('foto_curso')  # 👈 Recibir imagen
        Curso.objects.create(
            Nombre=nombre, 
            Creditos=creditos, 
            Estado=estado,
            foto_curso=foto  # 👈 Guardar imagen
            )
        return redirect('frontend_appescuela:ver_cursos')
    return render(request, 'frontend_appescuela/crear_curso.html')

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.Nombre = request.POST.get('Nombre')
        curso.Creditos = request.POST.get('Creditos')
        curso.Estado = request.POST.get('Estado') == 'on'
        nueva_foto = request.FILES.get('foto_curso')
        if nueva_foto:
            curso.foto_curso = nueva_foto  # 👈 Actualizar imagen si se proporciona       
        curso.save()
        return redirect('frontend_appescuela:ver_cursos')
    return render(request, 'frontend_appescuela/editar_curso.html', {'curso': curso})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('frontend_appescuela:ver_cursos')
    return render(request, 'frontend_appescuela/eliminar_curso.html', {'curso': curso})

# Matrículas
def listado_matricula(request):
    matriculas = Matricula.objects.all()
    return render(request, 'frontend_appescuela/listado_matricula.html', {'matriculas': matriculas})

def crear_matricula(request):
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        alumno_id = request.POST.get('Alumno')
        curso_id = request.POST.get('Curso')
        Matricula.objects.create(Alumno_id=alumno_id, Curso_id=curso_id)
        return redirect('frontend_appescuela:listado_matricula')
    return render(request, 'frontend_appescuela/crear_matricula.html', {
        'alumnos': alumnos,
        'cursos': cursos
    })

def eliminar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    if request.method == 'POST':
        matricula.delete()
        return redirect('frontend_appescuela:listado_matricula')
    return render(request, 'frontend_appescuela/eliminar_matricula.html', {'matricula': matricula})