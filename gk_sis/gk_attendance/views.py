from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Student, SchoolClass, Attendance
from .serializers import TeacherSerializer, StudentSerializer, SchoolClassSerializer, AttendanceSerializer
# Create your views here.


class TeacherViewSet(viewsets.ModelViewSet):
    """ endpoint for Teachers """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ endpoint for Students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolClassViewSet(viewsets.ModelViewSet):
    """ endpoint for SchoolClass """
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    """ endpoint for Attendance """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


def student_attendance_by_class(request):
    pass


def student_attendance_by_grade(request):
    pass


def student_attendance(request):
    pass

def index(request):
    return render(request, 'gk_attendance/index.html', {})
