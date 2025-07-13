from django.urls import path
from . import views

app_name = 'frontend_appescuela'  # 👈 Definimos el namespace (importante si lo usas en include)

urlpatterns = [
    # ————————————————————————
    # 🏠 Página de inicio
    # ————————————————————————
    path('', views.inicio, name='inicio'),

    # ————————————————————————
    # 👨‍🎓 CRUD Alumnos
    # ————————————————————————
    path('alumnos/', views.ver_alumnos, name='ver_alumnos'),
    path('alumno/<int:id>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumno/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('alumno/editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('alumno/eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),

    # ————————————————————————
    # 📘 CRUD Cursos
    # ————————————————————————
    path('cursos/', views.ver_cursos, name='ver_cursos'),
    path('curso/<int:id>/', views.detalle_curso, name='detalle_curso'),
    path('curso/nuevo/', views.crear_curso, name='crear_curso'),
    path('curso/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('curso/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),

    # ————————————————————————
    # 📚 CRUD Matrículas
    # ————————————————————————
    path('matriculas/', views.listado_matricula, name='listado_matricula'),
    path('matricula/nuevo/', views.crear_matricula, name='crear_matricula'),
    path('matricula/eliminar/<int:id>/', views.eliminar_matricula, name='eliminar_matricula'),
]