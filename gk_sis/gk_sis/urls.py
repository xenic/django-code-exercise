"""gk_sis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gk_attendance import views

router = routers.DefaultRouter()
router.register(r'teacher', views.TeacherViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'school_class', views.SchoolClassViewSet)

#for this project, no need to split out urls by app for now.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url('^attendanceList/(?P<school_class_id>.+)/$', views.AttendanceListViewSet.as_view({'get': 'retrieve'})),
    url(r'^admin/', admin.site.urls),
]
