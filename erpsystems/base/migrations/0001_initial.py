# Generated by Django 5.1.2 on 2024-10-13 16:11

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('date_of_birthday', models.DateField()),
                ('gender', models.CharField(choices=[('Чоловік', 'Чоловік'), ('Жінка', 'Жінка')], max_length=255)),
                ('residential_address', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=255)),
                ('hiring_date', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Працює', 'Працює'), ('У відпустці', 'У відпустці'), ('На лікарняному', 'На лікарняному')], max_length=255)),
                ('schedule', models.CharField(choices=[('Повний день', 'Повний день'), ('Перша зміна', 'Перша зміна'), ('Друга зміна', 'Друга зміна')], max_length=255)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('date_order', models.DateField()),
                ('status', models.CharField(choices=[('Не розпочато', 'Не розпочато'), ('У процесі', 'У процесі'), ('Завершено', 'Завершено')], max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('client_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('client_email', models.CharField(max_length=255)),
                ('delivery_address', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('total_payable', models.IntegerField()),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('Виплачено', 'Виплачено'), ('Не виплачено', 'Не виплачено')], max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Не розпочато', 'Не розпочато'), ('У процесі', 'У процесі'), ('Завершено', 'Завершено')], max_length=255)),
                ('priority', models.CharField(choices=[('Низький', 'Низький'), ('Середній', 'Середній'), ('Високий', 'Високий')], max_length=255)),
                ('description', models.TextField()),
                ('date_start', models.DateField()),
                ('date_finish', models.DateField()),
                ('progress', models.IntegerField()),
                ('comments', models.TextField()),
                ('slug', models.SlugField()),
                ('employee', models.ManyToManyField(to='base.employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
