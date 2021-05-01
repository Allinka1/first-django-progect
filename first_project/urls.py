"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from first_application.views import first_func, second_func, third_func, new_func
from second_application.views import first_second_func, second_second_func, third_second_func


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/<int:first>/', first_func),
    path('second/<int:second>/', second_func),
    path('third/<int:third>/', third_func),
    path('first_second/', first_second_func),
    path('second_second/', second_second_func),
    path('third_second/', third_second_func),
    path('new_func/<str:new>/', new_func)
]
