from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.db.utils import IntegrityError
# Create your views here.
def main(request):
    return render(request, 'main/main.html')
def contactus(request):
    return render(request, 'main/contactus.html')
def product(request):
    return render(request, 'main/product.html')
def implementation(request):
    return render(request, 'main/implementation.html')
def consultation(request):
    return render(request, 'main/consultation.html')
def support(request):
    return render(request, 'main/support.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if name and username and password and surname and repeat_password:
            if len(password) >= 8:
                if password == repeat_password:
                    try:
                        User.objects.create_user(first_name = name, username=username, last_name = surname, password = password)
                        return JsonResponse({'isRegister': True, 'name':name})
                    except IntegrityError:
                        return JsonResponse({'error': 'Такий користувач вже існує!'})
                else:
                    return JsonResponse({'error': 'Паролі не співпадають!'})
            else:
                return JsonResponse({'error': 'Пароль повинен бути більше ніж 7 символів!'})
        else:
            return JsonResponse({'error': 'Ви не заповнили усі поля!'})
def auth(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Ти вже авторизувався'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(password = password, username = username)
            print(user)
            if user:
                print('login success')
                login(request, user)
                return JsonResponse({'isLogin': True, 'username': username})
            else:
                return JsonResponse({'error': 'Логін aбо пароль невірний'})
        else:
            return JsonResponse({'error': 'Заповніть всі поля'})