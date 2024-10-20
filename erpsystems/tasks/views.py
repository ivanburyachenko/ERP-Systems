from django.shortcuts import render
from base.views import Task, Employee
# Create your views here.
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    statuses = []
    priorities = []
    for i in tasks:
        if i.status not in statuses:
            statuses.append(i.status)
        if i.priority not in priorities:
            priorities.append(i.priority)
    context = {'tasks':tasks, 'statuses': statuses, 'priorities':priorities}
    return render(request, 'tasks/tasks.html', context)
def task(request, slug):
    task = Task.objects.get(slug=slug)
    context = {'task':task}
    return render(request, 'tasks/task.html',context)
def filter_tasks(request):
    sort_by = request.GET.get('filter')
    number = request.GET.get('number')
    date_start = request.GET.get('date_start')
    progress = request.GET.get('progress')
    filter_by = request.GET.get('filter')
    filter_value = request.GET.get('value')

    tasks = Task.objects.all()
    if sort_by == 'number':
        if number == 'asc':
            tasks = tasks.order_by('number')
        else:
            tasks = tasks.order_by('-number')
    elif sort_by == 'date_start':
        if date_start == 'asc':
            tasks = tasks.order_by('date_start')
        else:
            tasks = tasks.order_by('-date_start')
    elif sort_by == 'progress':
        if progress == 'asc':
            tasks = tasks.order_by('progress')
        else:
            tasks = tasks.order_by('-progress')
    elif filter_by == 'статус':
        tasks = tasks.filter(status=filter_value)
    elif filter_by == 'пріорітет':
        tasks = tasks.filter(priority=filter_value)
    return render(request, 'tasks/listtasks.html', {'tasks': tasks})