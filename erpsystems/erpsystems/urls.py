"""
URL configuration for erpsystems project.

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
from main.views import *
from base.views import *
from salary.views import *
from selling.views import *
from accounting.views import *
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('contactus/', contactus, name='contactus'),
    path('product/', product, name='product'),
    path('implementation/', implementation, name='implementation'),
    path('consultation/', consultation, name='consultation'),
    path('support/', support, name='support'),
    path('register/', register, name='register'),
    path('auth/',auth, name='auth'),
    path('personal/', personal, name='personal'),
    path('accounting/', accounting, name='accounting'),
    path('salary/', salary, name='salary'),
    path('selling/', selling, name='selling'),
    path('tasks/', tasks, name='tasks'),
    path('employee/<slug>', employee, name='employee'),
    path('task/<slug>', task, name='task'),
    path('order/<slug>', order, name='order')
]
