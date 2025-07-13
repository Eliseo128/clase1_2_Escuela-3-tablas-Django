from django.db import models

class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    NumControl = models.CharField(max_length=8, unique=True)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    foto_alumno = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def NombreCompleto(self):
        return f"{self.ApellidoPaterno} {self.ApellidoMaterno}, {self.Nombres}"

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)
    foto_curso = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return f"{self.Nombre} ({self.Creditos})"

class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Alumno} => {self.Curso.Nombre}"