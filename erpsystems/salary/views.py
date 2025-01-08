from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.models import Salary, Employee
from django.shortcuts import get_object_or_404

# Create your views here.
def salary(request):
    salaries = Salary.objects.all()
    employees = Employee.objects.all()
    return render(request, 'salary/salary.html', {'salaries': salaries, 'employees': employees})
@csrf_exempt
def update_salary(request, id):
    if request.method == 'POST':
        salary = Salary.objects.get(id=id)
        salary.amount = request.POST.get('amount')
        salary.status = request.POST.get('status')
        salary.date = request.POST.get('date')
        salary.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})
@csrf_exempt
def delete_salary(request, id):
    if request.method == 'POST':
        salary = Salary.objects.get(id=id)
        salary.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})
@csrf_exempt
def add_salary(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        status = request.POST.get('status')
        employee = get_object_or_404(Employee, id=employee_id)
        Salary.objects.create(employee=employee, amount=amount, date=date, status=status, user=request.user)
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'fail'})