from django.shortcuts import render

# Create your views here.
def salary(request):
    return render(request, 'salary/salary.html')