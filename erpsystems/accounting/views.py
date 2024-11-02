from django.shortcuts import render
from base.models import Employee, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
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
    sort_by = request.GET.get('filter') 
    order = request.GET.get('order')
    filter_by = request.GET.get('filter')
    filter_value = request.GET.get('value')

    employees = Employee.objects.all()
    if sort_by == 'name':
        if order == 'asc':
            employees = employees.order_by('first_name')
        else:
            employees = employees.order_by('-first_name')
    elif sort_by == 'hiring_date':
        if order == 'asc':
            employees = employees.order_by('hiring_date')
        else:
            employees = employees.order_by('-hiring_date')
    if filter_by == 'посада':
        employees = employees.filter(position=filter_value)
    elif filter_by == 'статус':
        employees = employees.filter(status=filter_value)
    elif filter_by == 'розклад':
        employees = employees.filter(schedule=filter_value)
    return render(request, 'accounting/listemployees.html', {'employees': employees})

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        # Extract data from the request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        patronymic = request.POST.get('patronymic')
        date_of_birthday = request.POST.get('date_of_birthday')
        gender = request.POST.get('gender')
        residential_address = request.POST.get('residential_address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        position = request.POST.get('position')
        hiring_date = request.POST.get('hiring_date')
        status = request.POST.get('status')
        schedule = request.POST.get('schedule')

        # Create and save the new employee
        employee = Employee.objects.create(
            user=request.user,  # Adjust as needed
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            date_of_birthday=date_of_birthday,
            gender=gender,
            residential_address=residential_address,
            phone_number=phone_number,
            email=email,
            position=position,
            hiring_date=hiring_date,
            status=status,
            schedule=schedule,
            slug=f"{first_name}-{last_name}"
        )
        return JsonResponse({'status': 'success', 'employee_id': employee.id})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})