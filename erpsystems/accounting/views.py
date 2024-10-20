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

def filter_employees(request):
    sort_by = request.GET.get('filter')  # Изменено на 'filter'
    order = request.GET.get('order')
    filter_by = request.GET.get('filter')
    filter_value = request.GET.get('value')

    employees = Employee.objects.all()

    # Сортировка по имени
    if sort_by == 'name':
        if order == 'asc':
            employees = employees.order_by('first_name')
        else:
            employees = employees.order_by('-first_name')

    # Сортировка по дате приёма
    elif sort_by == 'hiring_date':
        if order == 'asc':
            employees = employees.order_by('hiring_date')
        else:
            employees = employees.order_by('-hiring_date')

    # Фильтрация по позиции
    if filter_by == 'посада':
        employees = employees.filter(position=filter_value)

    # Фильтрация по статусу
    elif filter_by == 'статус':
        employees = employees.filter(status=filter_value)

    # Фильтрация по расписанию
    elif filter_by == 'розклад':
        employees = employees.filter(schedule=filter_value)
    return render(request, 'accounting/listemployees.html', {'employees': employees})