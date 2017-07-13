from django.db import models


class Grade(models.Model):
    """ A model for storing grades (e.g. K, 1, 2, ..., 12, Freshman) in the school. """
    name = models.CharField(max_length=50)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade)


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)


class AttendanceStatus(models.Model):
    name = models.CharField(max_length=50)


class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    status = models.ForeignKey(AttendanceStatus)
