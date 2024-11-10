from django.shortcuts import render
from base.views import Task, Employee
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    employees = Employee.objects.all()
    statuses = []
    priorities = []
    for i in tasks:
        if i.status not in statuses:
            statuses.append(i.status)
        if i.priority not in priorities:
            priorities.append(i.priority)
    context = {'tasks':tasks, 'statuses': statuses, 'priorities':priorities, 'employees':employees}
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
def add_task(request):
    if request.method == 'POST':
        task = Task(
            user=request.user,
            status=request.POST.get('status'),
            priority=request.POST.get('priority'),
            description=request.POST.get('description'),
            date_start=request.POST.get('date_start'),
            date_finish=request.POST.get('date_finish'),
            progress=request.POST.get('progress'),
            comments=request.POST.get('comments'),
        )
        task.save()

        employee_ids = request.POST.getlist('employee')
        for employee_id in employee_ids:
            task.employee.add(employee_id)
        
        task.slug = f"{task.description}-{task.number}"
        task.save()
        
        return JsonResponse({'success': True})

    return render(request, 'your_template.html')
@csrf_exempt
def get_task(request, task_id):
    try:
        task = Task.objects.get(number=task_id)
        data = {
            'status': task.status,
            'priority': task.priority,
            'description': task.description,
            'date_start': task.date_start,
            'date_finish': task.date_finish,
            'progress': task.progress,
            'comments': task.comments,
        }
        return JsonResponse(data)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(number=task_id)
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.description = request.POST.get('description')
        task.date_start = request.POST.get('date_start')
        task.date_finish = request.POST.get('date_finish')
        task.progress = request.POST.get('progress')
        task.comments = request.POST.get('comments')
        task.save()
        data = {
            'status': task.status,
            'priority': task.priority,
            'description': task.description,
            'date_start': task.date_start,
            'date_finish': task.date_finish,
            'progress': task.progress,
            'comments': task.comments,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)