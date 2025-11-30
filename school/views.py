from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import GradeRecord

@login_required
def student_diary(request):
    if not hasattr(request.user, 'student'):
        return HttpResponseForbidden("Доступ разрешён только ученикам.")
    
    records = GradeRecord.objects.filter(student=request.user.student).order_by('-date')
    return render(request, 'school/student_diary.html', {'records': records})

@login_required
def parent_diary(request):
    if not hasattr(request.user, 'parent'):
        return HttpResponseForbidden("Доступ разрешён только родителям.")
    
    records = GradeRecord.objects.filter(
        student__in=request.user.parent.students.all()
    ).order_by('-date')
    return render(request, 'school/parent_diary.html', {'records': records})

@login_required
def teacher_journal(request):
    if not hasattr(request.user, 'teacher'):
        return HttpResponseForbidden("Доступ разрешён только учителям.")
    
    records = GradeRecord.objects.filter(
        lesson__teacher=request.user.teacher
    ).order_by('-date')
    return render(request, 'school/teacher_journal.html', {'records': records})

def home(request):
    return render(request, 'school/home.html', {'user': request.user})