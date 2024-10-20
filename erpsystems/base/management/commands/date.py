from base.models import Employee, Task, Product, Order, Salary, User
import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generate random data for the database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()

        # Create Employees
        for _ in range(10):  # Adjust the number of employees
            user = random.choice(users)
            employee = Employee.objects.create(
                user=user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                patronymic=fake.first_name(),
                date_of_birthday=fake.date_of_birth(minimum_age=18, maximum_age=65),
                gender=random.choice(['Чоловік', 'Жінка']),
                residential_address=fake.address(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                position=random.choice(['Менеджер', 'Розробник', 'Дизайнер']),
                hiring_date=fake.date(),
                status=random.choice(['Працює', 'У відпустці', 'На лікарняному']),
                schedule=random.choice(['Повний день', 'Перша зміна', 'Друга зміна']),
                slug=fake.slug()
            )

        # Create Tasks
        for _ in range(20):  # Adjust the number of tasks
            user = random.choice(users)
            task = Task.objects.create(
                user=user,
                status=random.choice(['Не розпочато', 'У процесі', 'Завершено']),
                priority=random.choice(['Низький', 'Середній', 'Високий']),
                description=fake.text(),
                date_start=fake.date_this_month(),
                date_finish=fake.date_this_month(),
                progress=random.randint(0, 100),
                comments=fake.text(),
                slug=fake.slug()
            )
            task.employee.add(random.choice(Employee.objects.all()))

        # Create Products
        for _ in range(15):  # Adjust the number of products
            user = random.choice(users)
            Product.objects.create(
                user=user,
                name=fake.word(),
                price=random.randint(10, 500)
            )

        # Create Orders
        for _ in range(10):  # Adjust the number of orders
            user = random.choice(users)
            products = Product.objects.order_by('?')[:random.randint(1, 3)]
            total_price = sum(product.price for product in products)

            order = Order.objects.create(
                user=user,
                date_order=fake.date(),
                status=random.choice(['Не розпочато', 'У процесі', 'Завершено']),
                client_name=fake.name(),
                client_phone_number=fake.phone_number(),
                client_email=fake.email(),
                delivery_address=fake.address(),
                price=total_price,
                discount=random.randint(0, 50),  # Assuming discount is a percentage
                total_payable=total_price * (1 - (random.randint(0, 50) / 100)),
                slug=fake.slug()
            )
            order.products.set(products)

        # Create Salaries
        for _ in range(10):  # Adjust the number of salaries
            user = random.choice(users)
            employee = random.choice(Employee.objects.all())
            Salary.objects.create(
                user=user,
                employee=employee,
                amount=random.randint(1000, 5000),  # Assuming salary amount
                status=random.choice(['Виплачено', 'Не виплачено'])
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated random data'))
