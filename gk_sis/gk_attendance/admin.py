from django.contrib import admin
from .models import Teacher, Student, SchoolClass, AttendanceStatus
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(SchoolClass)
admin.site.register(AttendanceStatus)
