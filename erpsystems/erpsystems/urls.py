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
    path('order/<slug>', order, name='order'),
    path('filter_employees/', filter_employees, name='filter_employees'),
    path('filter_orders/', filter_orders, name='filter_orders'),
    path('filter_tasks/', filter_tasks, name='filter_tasks'),
    path('update_salary/<int:id>/', update_salary, name='update_salary'),
    path('delete_salary/<int:id>/', delete_salary, name='delete_salary'),
    path('add_salary/', add_salary, name='add_salary'),
    path('add_employee/', add_employee, name='add_employee'),
    path('add_order/', add_order, name='add_order'),
    path('add_task/', add_task, name='add_task'),
    path('get-employee/<int:employee_id>/', get_employee, name='get_employee'),
    path('update-employee/<int:employee_id>/', update_employee, name='update_employee'),
    path('get-order/<int:order_id>/', get_order, name='get_order'),
    path('update-order/<int:order_id>/', update_order, name='update_order'),
    path('get-task/<int:task_id>/', get_task, name='get_task'),
    path('update-task/<int:task_id>/', update_task, name='update_task'),
]
