from django.shortcuts import render
from base.views import Task, Employee
# Create your views here.
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks':tasks}
    return render(request, 'tasks/tasks.html', context)
def task(request, slug):
    task = Task.objects.get(slug=slug)
    context = {'task':task}
    return render(request, 'tasks/task.html',context)