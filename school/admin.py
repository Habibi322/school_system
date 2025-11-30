from django.contrib import admin
from .models import Grade, Student, Parent, Teacher, ClassTeacher, Lesson, GradeRecord

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('number', 'specialization')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('students',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')

@admin.register(ClassTeacher)
class ClassTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'grade')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'grade', 'teacher', 'day_of_week', 'period')
    list_filter = ('grade', 'day_of_week')

@admin.register(GradeRecord)
class GradeRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'score', 'date')
    list_filter = ('date', 'lesson__grade')