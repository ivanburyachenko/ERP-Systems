from django.shortcuts import render
from base.models import Employee, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from phonenumber_field.modelfields import PhoneNumber
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

        employee = Employee.objects.create(
            user=request.user,
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

@csrf_exempt
def get_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        data = {
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'patronymic': employee.patronymic,
            'date_of_birthday': employee.date_of_birthday.strftime('%Y-%m-%d'),
            'gender': employee.gender,
            'residential_address': employee.residential_address,
            'phone_number': str(employee.phone_number),
            'email': employee.email,
            'position': employee.position,
            'hiring_date': employee.hiring_date,
            'status': employee.status,
            'schedule': employee.schedule,
        }
        return JsonResponse(data)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)

def update_employee(request, employee_id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=employee_id)
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.patronymic = request.POST.get('patronymic')
        employee.date_of_birthday = request.POST.get('date_of_birthday')
        employee.gender = request.POST.get('gender')
        employee.residential_address = request.POST.get('residential_address')
        employee.phone_number = request.POST.get('phone_number')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.hiring_date = request.POST.get('hiring_date')
        employee.status = request.POST.get('status')
        employee.schedule = request.POST.get('schedule')
        employee.save()
        return JsonResponse({
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'patronymic': employee.patronymic,
            'date_of_birthday': employee.date_of_birthday,
            'gender': employee.gender,
            'residential_address': employee.residential_address,
            'phone_number': str(employee.phone_number),
            'email': employee.email,
            'position': employee.position,
            'hiring_date': employee.hiring_date,
            'status': employee.status,
            'schedule': employee.schedule,
        })