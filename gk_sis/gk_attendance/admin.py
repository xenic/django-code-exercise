from django.contrib import admin
from .models import Teacher, Student, SchoolClass, AttendanceStatus, Grade
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(SchoolClass)
admin.site.register(AttendanceStatus)
admin.site.register(Grade)
