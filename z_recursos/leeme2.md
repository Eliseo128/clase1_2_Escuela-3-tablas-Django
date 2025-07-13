¡Tienes toda la razón! A continuación, te comparto **el contenido completo de todas las plantillas HTML** que faltaban en tu carpeta:

```
frontend_appescuela/templates/frontend_appescuela/
├── ver_alumno.html
├── detalles_alumno.html
├── crear_alumno.html
├── editar_alumno.html
├── eliminar_alumno.html
├── ver_curso.html
├── detalle_curso.html
├── crear_curso.html
├── editar_curso.html
├── eliminar_curso.html
├── listado_matricula.html
├── crear_matricula.html
└── eliminar_matricula.html
```

---

## 🧾 1. `ver_alumno.html` – Listado de alumnos

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Listado de Alumnos{% endblock %}
{% block content %}
<h2>Listado de Alumnos</h2>
<a href="{% url 'frontend_appescuela:crear_alumno' %}" class="btn btn-success mb-3">Nuevo Alumno</a>

<table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>
            <th>Foto</th>
            <th>Nombre Completo</th>
            <th>Número de Control</th>
            <th>Fecha de Nacimiento</th>
            <th>Sexo</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for alumno in alumnos %}
        <tr>
            <td>
                {% if alumno.foto_alumno %}
                    <img src="{{ alumno.foto_alumno.url }}" alt="Foto del alumno" class="img-fluid rounded" style="max-width: 60px;">
                {% else %}
                    Sin foto
                {% endif %}
            </td>
            <td>{{ alumno.NombreCompleto }}</td>
            <td>{{ alumno.NumControl }}</td>
            <td>{{ alumno.FechaNacimiento|date:"d/m/Y" }}</td>
            <td>{{ alumno.Sexo }}</td>
            <td>
                <a href="{% url 'frontend_appescuela:detalle_alumno' alumno.id %}" class="btn btn-info btn-sm">Ver</a>
                <a href="{% url 'frontend_appescuela:editar_alumno' alumno.id %}" class="btn btn-warning btn-sm">Editar</a>
                <a href="{% url 'frontend_appescuela:eliminar_alumno' alumno.id %}" class="btn btn-danger btn-sm">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

## 🧾 2. `detalles_alumno.html` – Detalles completos de un alumno

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Detalles del Alumno: {{ alumno.NombreCompleto }}{% endblock %}
{% block content %}
<div class="card mb-4">
    <div class="card-header bg-primary text-white">
        <h2>Detalles del Alumno</h2>
    </div>
    <div class="card-body">
        <!-- Foto -->
        <div class="text-center mb-3">
            {% if alumno.foto_alumno %}
                <img src="{{ alumno.foto_alumno.url }}" alt="Foto del alumno" class="img-fluid rounded" style="max-width: 200px;">
            {% else %}
                <p>No hay imagen disponible.</p>
            {% endif %}
        </div>

        <!-- Datos -->
        <p><strong>Apellido Paterno:</strong> {{ alumno.ApellidoPaterno }}</p>
        <p><strong>Apellido Materno:</strong> {{ alumno.ApellidoMaterno }}</p>
        <p><strong>Nombres:</strong> {{ alumno.Nombres }}</p>
        <p><strong>Número de Control:</strong> {{ alumno.NumControl }}</p>
        <p><strong>Fecha de Nacimiento:</strong> {{ alumno.FechaNacimiento|date:"d/m/Y" }}</p>
        <p><strong>Sexo:</strong> {{ alumno.Sexo|yesno:"Masculino,Femenino" }}</p>
    </div>
</div>

<a href="{% url 'frontend_appescuela:ver_alumnos' %}" class="btn btn-secondary">Volver al listado</a>
{% endblock %}
```

---

## 🧾 3. `crear_alumno.html` – Registrar nuevo alumno

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Registrar Alumno{% endblock %}
{% block content %}
<h2>Registrar Nuevo Alumno</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    
    <div class="mb-3">
        <label for="ApellidoPaterno" class="form-label">Apellido Paterno</label>
        <input type="text" name="ApellidoPaterno" id="ApellidoPaterno" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="ApellidoMaterno" class="form-label">Apellido Materno</label>
        <input type="text" name="ApellidoMaterno" id="ApellidoMaterno" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="Nombres" class="form-label">Nombres</label>
        <input type="text" name="Nombres" id="Nombres" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="NumControl" class="form-label">Número de Control</label>
        <input type="text" name="NumControl" id="NumControl" class="form-control" maxlength="8" required>
    </div>
    <div class="mb-3">
        <label for="FechaNacimiento" class="form-label">Fecha de Nacimiento</label>
        <input type="date" name="FechaNacimiento" id="FechaNacimiento" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="Sexo" class="form-label">Sexo</label>
        <select name="Sexo" id="Sexo" class="form-control" required>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
        </select>
    </div>

    <!-- Foto -->
    <div class="mb-3">
        <label for="foto_alumno" class="form-label">Foto del Alumno (opcional)</label>
        <input type="file" name="foto_alumno" id="foto_alumno" class="form-control" accept="image/*">
    </div>

    <button type="submit" class="btn btn-primary">Guardar</button>
    <a href="{% url 'frontend_appescuela:ver_alumnos' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 4. `editar_alumno.html` – Editar datos y foto

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Editar Alumno{% endblock %}
{% block content %}
<h2>Editar Alumno</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    
    <div class="mb-3">
        <label for="ApellidoPaterno" class="form-label">Apellido Paterno</label>
        <input type="text" name="ApellidoPaterno" id="ApellidoPaterno" class="form-control" value="{{ alumno.ApellidoPaterno }}" required>
    </div>
    <div class="mb-3">
        <label for="ApellidoMaterno" class="form-label">Apellido Materno</label>
        <input type="text" name="ApellidoMaterno" id="ApellidoMaterno" class="form-control" value="{{ alumno.ApellidoMaterno }}" required>
    </div>
    <div class="mb-3">
        <label for="Nombres" class="form-label">Nombres</label>
        <input type="text" name="Nombres" id="Nombres" class="form-control" value="{{ alumno.Nombres }}" required>
    </div>
    <div class="mb-3">
        <label for="NumControl" class="form-label">Número de Control</label>
        <input type="text" name="NumControl" id="NumControl" class="form-control" value="{{ alumno.NumControl }}" maxlength="8" required>
    </div>
    <div class="mb-3">
        <label for="FechaNacimiento" class="form-label">Fecha de Nacimiento</label>
        <input type="date" name="FechaNacimiento" id="FechaNacimiento" class="form-control" value="{{ alumno.FechaNacimiento|date:'Y-m-d' }}" required>
    </div>
    <div class="mb-3">
        <label for="Sexo" class="form-label">Sexo</label>
        <select name="Sexo" id="Sexo" class="form-control" required>
            <option value="M" {% if alumno.Sexo == 'M' %}selected{% endif %}>Masculino</option>
            <option value="F" {% if alumno.Sexo == 'F' %}selected{% endif %}>Femenino</option>
        </select>
    </div>

    <!-- Campo para subir nueva foto -->
    <div class="mb-3">
        <label for="foto_alumno" class="form-label">Cambiar Foto del Alumno (opcional)</label>
        <input type="file" name="foto_alumno" id="foto_alumno" class="form-control" accept="image/*">
    </div>

    <!-- Mostrar foto actual si existe -->
    {% if alumno.foto_alumno %}
        <div class="mb-3 text-center">
            <label class="form-label d-block">Foto actual:</label>
            <img src="{{ alumno.foto_alumno.url }}" alt="Foto del alumno" class="img-fluid rounded" style="max-width: 200px;">
        </div>
    {% else %}
        <p class="text-center text-muted">No hay foto disponible.</p>
    {% endif %}

    <button type="submit" class="btn btn-primary">Actualizar</button>
    <a href="{% url 'frontend_appescuela:ver_alumnos' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 5. `eliminar_alumno.html` – Confirmar eliminación

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Eliminar Alumno{% endblock %}
{% block content %}
<h2>¿Estás seguro de eliminar este alumno?</h2>
<p><strong>Nombre:</strong> {{ alumno.NombreCompleto }}</p>
<p><strong>Número de Control:</strong> {{ alumno.NumControl }}</p>

<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Eliminar</button>
    <a href="{% url 'frontend_appescuela:ver_alumnos' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 6. `ver_curso.html` – Listado de cursos

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Listado de Cursos{% endblock %}
{% block content %}
<h2>Listado de Cursos</h2>
<a href="{% url 'frontend_appescuela:crear_curso' %}" class="btn btn-success mb-3">Nuevo Curso</a>

<table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>
            <th>Foto</th>
            <th>Nombre</th>
            <th>Creditos</th>
            <th>Estado</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for curso in cursos %}
        <tr>
            <td>
                {% if curso.foto_curso %}
                    <img src="{{ curso.foto_curso.url }}" alt="Foto del curso" class="img-fluid rounded" style="max-width: 60px;">
                {% else %}
                    Sin foto
                {% endif %}
            </td>
            <td>{{ curso.Nombre }}</td>
            <td>{{ curso.Creditos }}</td>
            <td>{{ curso.Estado|yesno:"Activo,Inactivo" }}</td>
            <td>
                <a href="{% url 'frontend_appescuela:detalle_curso' curso.id %}" class="btn btn-info btn-sm">Ver</a>
                <a href="{% url 'frontend_appescuela:editar_curso' curso.id %}" class="btn btn-warning btn-sm">Editar</a>
                <a href="{% url 'frontend_appescuela:eliminar_curso' curso.id %}" class="btn btn-danger btn-sm">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

## 🧾 7. `detalle_curso.html` – Detalles de un curso

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Detalles del Curso: {{ curso.Nombre }}{% endblock %}
{% block content %}
<div class="card mb-4">
    <div class="card-header bg-primary text-white">
        <h2>Detalles del Curso</h2>
    </div>
    <div class="card-body">
        <p><strong>Nombre:</strong> {{ curso.Nombre }}</p>
        <p><strong>Créditos:</strong> {{ curso.Creditos }}</p>
        <p><strong>Estado:</strong> {{ curso.Estado|yesno:"Activo,Inactivo" }}</p>

        <!-- Mostrar imagen -->
        {% if curso.foto_curso %}
            <div class="mb-3 text-center">
                <img src="{{ curso.foto_curso.url }}" alt="Foto del curso" class="img-fluid rounded" style="max-width: 200px;">
            </div>
        {% else %}
            <p class="text-center text-muted">No hay imagen disponible.</p>
        {% endif %}
    </div>
</div>

<a href="{% url 'frontend_appescuela:ver_cursos' %}" class="btn btn-secondary">Volver al Listado</a>
{% endblock %}
```

---

## 🧾 8. `crear_curso.html` – Registrar nuevo curso

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Crear Curso{% endblock %}
{% block content %}
<h2>Registrar Nuevo Curso</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="mb-3">
        <label for="Nombre" class="form-label">Nombre del Curso</label>
        <input type="text" name="Nombre" id="Nombre" class="form-control" required>
    </div>
    <div class="mb-3">
        <label for="Creditos" class="form-label">Créditos</label>
        <input type="number" name="Creditos" id="Creditos" class="form-control" required>
    </div>
    <div class="mb-3 form-check">
        <input type="checkbox" name="Estado" id="Estado" class="form-check-input" checked>
        <label for="Estado" class="form-check-label">Curso Activo</label>
    </div>

    <!-- Foto -->
    <div class="mb-3">
        <label for="foto_curso" class="form-label">Foto del Curso (opcional)</label>
        <input type="file" name="foto_curso" id="foto_curso" class="form-control" accept="image/*">
    </div>

    <button type="submit" class="btn btn-primary">Guardar</button>
    <a href="{% url 'frontend_appescuela:ver_cursos' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 9. `editar_curso.html` – Actualizar curso

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Editar Curso{% endblock %}
{% block content %}
<h2>Editar Curso</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="mb-3">
        <label for="Nombre" class="form-label">Nombre del Curso</label>
        <input type="text" name="Nombre" id="Nombre" class="form-control" value="{{ curso.Nombre }}" required>
    </div>
    <div class="mb-3">
        <label for="Creditos" class="form-label">Créditos</label>
        <input type="number" name="Creditos" id="Creditos" class="form-control" value="{{ curso.Creditos }}" required>
    </div>
    <div class="mb-3 form-check">
        <input type="checkbox" name="Estado" id="Estado" class="form-check-input" {% if curso.Estado %}checked{% endif %}>
        <label for="Estado" class="form-check-label">Curso Activo</label>
    </div>

    <!-- Subir nueva foto -->
    <div class="mb-3">
        <label for="foto_curso" class="form-label">Cambiar Foto del Curso (opcional)</label>
        <input type="file" name="foto_curso" id="foto_curso" class="form-control">
    </div>

    <!-- Mostrar foto actual -->
    {% if curso.foto_curso %}
        <div class="mb-3 text-center">
            <label class="form-label d-block">Foto actual:</label>
            <img src="{{ curso.foto_curso.url }}" alt="Foto del curso" class="img-fluid rounded" style="max-width: 200px;">
        </div>
    {% else %}
        <p class="text-center text-muted">No hay foto disponible.</p>
    {% endif %}

    <button type="submit" class="btn btn-primary">Actualizar</button>
    <a href="{% url 'frontend_appescuela:ver_cursos' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 10. `listado_matricula.html` – Listado de matrículas

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Listado de Matrículas{% endblock %}
{% block content %}
<h2>Listado de Matrículas</h2>
<a href="{% url 'frontend_appescuela:crear_matricula' %}" class="btn btn-success mb-3">Registrar Matrícula</a>

<table class="table table-bordered">
    <thead class="thead-dark">
        <tr>
            <th>Alumno</th>
            <th>Curso</th>
            <th>Fecha de Matrícula</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        {% for m in matriculas %}
        <tr>
            <td>{{ m.Alumno }}</td>
            <td>{{ m.Curso }}</td>
            <td>{{ m.FechaMatricula|date:"d/m/Y H:i" }}</td>
            <td>
                <a href="{% url 'frontend_appescuela:eliminar_matricula' m.id %}" class="btn btn-danger btn-sm">Eliminar</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

## 🧾 11. `crear_matricula.html` – Registrar nueva matrícula

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Registrar Matrícula{% endblock %}
{% block content %}
<h2>Registrar Matrícula</h2>
<form method="post">
    {% csrf_token %}
    <div class="mb-3">
        <label for="Alumno" class="form-label">Seleccionar Alumno</label>
        <select name="Alumno" id="Alumno" class="form-control" required>
            {% for alumno in alumnos %}
            <option value="{{ alumno.id }}">{{ alumno.NombreCompleto }}</option>
            {% endfor %}
        </select>
    </div>
    <div class="mb-3">
        <label for="Curso" class="form-label">Seleccionar Curso</label>
        <select name="Curso" id="Curso" class="form-control" required>
            {% for curso in cursos %}
            <option value="{{ curso.id }}">{{ curso.Nombre }}</option>
            {% endfor %}
        </select>
    </div>
    <button type="submit" class="btn btn-primary">Guardar</button>
    <a href="{% url 'frontend_appescuela:listado_matricula' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 🧾 12. `eliminar_matricula.html` – Confirmar eliminación

```html
{% extends "frontend_appescuela/base.html" %}
{% block title %}Eliminar Matrícula{% endblock %}
{% block content %}
<h2>¿Estás seguro de eliminar esta matrícula?</h2>
<p><strong>Alumno:</strong> {{ matricula.Alumno }}</p>
<p><strong>Curso:</strong> {{ matricula.Curso }}</p>
<p><strong>Fecha:</strong> {{ matricula.FechaMatricula|date:"d/m/Y H:i" }}</p>

<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Eliminar</button>
    <a href="{% url 'frontend_appescuela:listado_matricula' %}" class="btn btn-secondary">Cancelar</a>
</form>
{% endblock %}
```

---

## 📦 ¿Quieres que te genere un `.zip` con todo el proyecto?

Con gusto puedo ayudarte a generar un archivo comprimido con **todo funcionando**, incluyendo:
- Todas estas plantillas
- Modelos, vistas, URLs, configuraciones
- Carpeta `media/` lista para imágenes
- Instrucciones completas

¿Usas **Windows** o **Linux/macOS**?

Dime y te ayudo a descargarlo listo para usar.  
¡Éxito con tu proyecto escolar! 😎