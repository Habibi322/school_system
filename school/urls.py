from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← Главная страница
    path('student/diary/', views.student_diary, name='student_diary'),
    path('parent/diary/', views.parent_diary, name='parent_diary'),
    path('teacher/journal/', views.teacher_journal, name='teacher_journal'),
]