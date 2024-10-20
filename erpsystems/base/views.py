from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import *
# Create your views here.
def personal(request):
    employers=Employee.objects.filter(user=request.user)
    employers_new=Employee.objects.filter(user=request.user, hiring_date__gte=timezone.now() - timedelta(days=30))
    employers_rest=Employee.objects.filter(user=request.user, status__in=["У відпустці", "На лікарняному"])
    tasks=Task.objects.filter(user=request.user)
    tasks_ended=Task.objects.filter(user=request.user, status = "Завершено")
    tasks_overdue=Task.objects.filter(user=request.user, status__in = ["Не розпочато", "У процесі"], date_finish__lte = timezone.now())
    orders=Order.objects.filter(user=request.user)
    orders_new=Order.objects.filter(user=request.user, date_order__gte=timezone.now() - timedelta(days=30))
    orders_in_process=Order.objects.filter(user=request.user, status="У процесі")
    orders_total = 0
    for i in orders:
        orders_total+=i.total_payable
    salaries=Salary.objects.filter(user=request.user)
    salaries_get=Salary.objects.filter(user=request.user, status="Виплачено")
    salaries_month = 0
    for i in salaries:
        salaries_month+=i.amount
    context = {'employers':employers, 'tasks':tasks, 'tasks_ended':tasks_ended, 'tasks_overdue':tasks_overdue, 'orders':orders, 'orders_total':orders_total, 'orders_new':orders_new, 
               'orders_in_process':orders_in_process, 'salaries':salaries, 'salaries_month':salaries_month, 
               'salaries_get':salaries_get, 'employers_new':employers_new, 'employers_rest':employers_rest}
    return render(request, 'base/personal.html', context)