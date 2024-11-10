from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base.models import Salary

# Create your views here.
def salary(request):
    salaries = Salary.objects.all() 
    return render(request, 'salary/salary.html', {'salaries': salaries})
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