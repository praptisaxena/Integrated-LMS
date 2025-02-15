"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views,user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    path('', views.HOME, name='home'),

    path('single/course', views.SINGLE_COURSE, name='single_course'),

    path('contact', views.CONTACT_US, name='contact'),

    path('about_us', views.ABOUT_US, name='about_us'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register', user_login.REGISTER, name='register'),

    path('doLogin',user_login.DO_LOGIN,name='doLogin'),
]
