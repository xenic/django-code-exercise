from django.db import models


class Grade(models.Model):
    """ A model for storing grades (e.g. K, 1, 2, ..., 12, Freshman) in the school. """
    name = models.CharField(max_length=50)

    def __repr__(self):
        return "Grade(name='{}')".format(self.name)

    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.first_name, self.middle_name, self.last_name, self.grade)


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Many-to-Many relationship between student and teachers will be mapped through
    # classes...
    #students = models.ManyToManyField(Student)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return "{}".format(self.name)


class AttendanceStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}(name='{}')".format(self.__class__, self.name)


class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    status = models.ForeignKey(AttendanceStatus)

    def __str__(self):
        return "{} {} {} {}".format(self.student, self.date, self.school_class, self.status)
