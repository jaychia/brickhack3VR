"""clickr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^prof/(?P<professorName>[a-zA-Z]+)/(?P<class_label>[a-zA-Z0-9 _.-]+)/$', views.receiveName, name='receiveName'),
	url(r'^prof/(?P<professorName>[a-zA-Z]+)/(?P<class_label>[a-zA-Z0-9 _.-]+)/posting$', views.receiveQuestion, name='receive_question'),
    url(r'^prof$', views.prof, name="prof_home"),
    url(r'^student$', views.student, name="student_home"),
    url(r'^student/(?P<studentName>[a-zA-Z]+)/(?P<class_label>[a-zA-Z0-9]+)/$', views.receiveStudentName, name='receiveStudentName'),
    url(r'^activate/(?P<questionID>[a-zA-Z0-9]+)/$', views.turnOnQuestion, name='turnOnQuestion'),
    url(r'^deactivate/(?P<questionID>[a-zA-Z0-9]+)/$', views.turnOffQuestion, name='turnOffQuestion'),
    url(r'^$', views.index, name="home"),
    url(r'^student/$', views.get_room, name="get_room"),
]

