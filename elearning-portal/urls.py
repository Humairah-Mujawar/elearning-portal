"""
URL configuration for elearning-portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus),
    path('courses/',views.course),
    path('courses/<int:courseid>', views.courseDetails),
    path('team/', views.ourteam),
    path('testimonial/', views.testimonial),
    path('contact/', views.contact),
    path('404/', views.pageNotFound)
]

handler404 = views.pageNotFound