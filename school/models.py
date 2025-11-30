from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    """Учебный класс (1–3) со специализацией"""
    number = models.PositiveSmallIntegerField(
        choices=[(1, '1 класс'), (2, '2 класс'), (3, '3 класс')],
        verbose_name="Номер класса"
    )
    specialization = models.CharField(max_length=100, verbose_name="Специализация")

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return f"{self.number} класс — {self.specialization}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Класс")

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.grade})"


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    students = models.ManyToManyField(Student, verbose_name="Дети")

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    def __str__(self):
        return self.user.get_full_name()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    subject = models.CharField(max_length=100, verbose_name="Предмет")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.subject}"


class ClassTeacher(models.Model):
    """Классный руководитель (один учитель — один класс)"""
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE, verbose_name="Класс")

    class Meta:
        verbose_name = "Классный руководитель"
        verbose_name_plural = "Классные руководители"

    def __str__(self):
        return f"{self.teacher} — классный руководитель {self.grade}"


class Lesson(models.Model):
    """Расписание: какой предмет, когда и у кого"""
    subject = models.CharField(max_length=100, verbose_name="Предмет")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Класс")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    day_of_week = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Понедельник'),
            (2, 'Вторник'),
            (3, 'Среда'),
            (4, 'Четверг'),
            (5, 'Пятница'),
        ],
        verbose_name="День недели"
    )
    period = models.PositiveSmallIntegerField(verbose_name="Номер урока")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.subject} — {self.grade}, {self.get_day_of_week_display()}, урок {self.period}"


class GradeRecord(models.Model):
    """Оценки и домашние задания"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Ученик")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    score = models.PositiveSmallIntegerField(
        null=True, blank=True,
        verbose_name="Оценка"
    )
    homework = models.TextField(blank=True, verbose_name="Домашнее задание")
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = "Запись в журнале"
        verbose_name_plural = "Записи в журнале"

    def __str__(self):
        return f"{self.student} — {self.lesson.subject} ({self.date})"