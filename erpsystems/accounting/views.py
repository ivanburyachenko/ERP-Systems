from django.shortcuts import render
from base.models import Employee, Task
# Create your views here.
def accounting(request):
    employees = Employee.objects.filter(user=request.user)
    positions = []
    statuses = []
    schedules = []
    for i in employees:
        if i.position not in positions:
            positions.append(i.position)
        if i.status not in statuses:
            statuses.append(i.status)
        if i.schedule not in schedules:
            schedules.append(i.schedule)
    context={'employees':employees, 'positions': positions, 'statuses':statuses, 'schedules': schedules}
    return render(request, 'accounting/accounting.html', context)
def employee(request, slug):
    employee = Employee.objects.get(slug=slug)
    tasks = Task.objects.filter(employee=employee)
    context = {'employee':employee, 'tasks': tasks}
    return render(request, 'accounting/employee.html',context)