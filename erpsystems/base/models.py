from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    date_of_birthday = models.DateField()
    gender = models.CharField(max_length=255, choices=[('Чоловік', 'Чоловік'), ('Жінка', 'Жінка')])
    residential_address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    position = models.CharField(max_length=255)
    hiring_date = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[('Працює', 'Працює'), ('У відпустці', 'У відпустці'), ('На лікарняному', 'На лікарняному')])
    schedule = models.CharField(max_length=255, choices=[('Повний день', 'Повний день'), ('Перша зміна', 'Перша зміна'), ('Друга зміна', 'Друга зміна')])
    slug = models.SlugField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, choices=[('Не розпочато', 'Не розпочато'), ('У процесі', 'У процесі'), ('Завершено', 'Завершено')])
    priority = models.CharField(max_length=255, choices=[('Низький', 'Низький'), ('Середній', 'Середній'), ('Високий', 'Високий')])
    description = models.TextField()
    employee = models.ManyToManyField(Employee)
    date_start = models.DateField()
    date_finish = models.DateField()
    progress = models.IntegerField()
    comments = models.TextField()
    slug = models.SlugField()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True)
    date_order = models.DateField()
    status = models.CharField(max_length=255, choices=[('Не розпочато', 'Не розпочато'), ('У процесі', 'У процесі'), ('Завершено', 'Завершено')])
    client_name = models.CharField(max_length=255)
    client_phone_number = PhoneNumberField()
    client_email = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.IntegerField()
    total_payable = models.IntegerField()
    products = models.ManyToManyField(Product)
    slug = models.SlugField()

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=255, choices=[('Виплачено', 'Виплачено'), ('Не виплачено', 'Не виплачено')])