from django.shortcuts import render
from base.views import Order, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def selling(request):
    orders = Order.objects.filter(user=request.user)
    products = Product.objects.all()
    statuses = []
    for i in orders:
        if i.status not in statuses:
            statuses.append(i.status)
    context = {'orders':orders, 'statuses': statuses, 'products':products}
    return render(request, 'selling/selling.html', context)
def order(request, slug):
    order = Order.objects.get(slug=slug)
    context={'order':order}
    return render(request, 'selling/order.html', context)
def filter_orders(request):
    sort_by = request.GET.get('filter')
    number = request.GET.get('number')
    client_email = request.GET.get('client_email')
    total_payable = request.GET.get('total_payable')
    date_order = request.GET.get('date_order')
    filter_by = request.GET.get('filter')
    filter_value = request.GET.get('value')

    orders = Order.objects.all()
    if sort_by == 'number':
        if number == 'asc':
            orders = orders.order_by('number')
        else:
            orders = orders.order_by('-number')
    elif sort_by == 'client_email':
        if client_email == 'asc':
            orders = orders.order_by('client_email')
        else:
            orders = orders.order_by('-client_email')
    elif sort_by == 'date_order':
        if date_order == 'asc':
            orders = orders.order_by('date_order')
        else:
            orders = orders.order_by('-date_order')
    elif sort_by == 'total_payable':
        if total_payable == 'asc':
            orders = orders.order_by('total_payable')
        else:
            orders = orders.order_by('-total_payable')
    
    elif filter_by == 'статус':
        orders = orders.filter(status=filter_value)
    return render(request, 'selling/listselling.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        order = Order(
            user=request.user,
            date_order=request.POST.get('date_order'),
            status=request.POST.get('status'),
            client_name=request.POST.get('client_name'),
            client_phone_number=request.POST.get('client_phone_number'),
            client_email=request.POST.get('client_email'),
            delivery_address=request.POST.get('delivery_address'),
            price=request.POST.get('price'),
            discount=request.POST.get('discount'),
            total_payable=request.POST.get('total_payable'),
        )
        order.save()
        product_ids = request.POST.getlist('products')
        for product_id in product_ids:
            order.products.add(product_id)
        order.slug = f"{order.client_name}-{order.number}"
        order.save()
        
        return JsonResponse({'success': True})

    return render(request, 'your_template.html') 

@csrf_exempt
def get_order(request, order_id):
    if request.method == 'GET':
        try:
            order = Order.objects.get(number=order_id)
            data = {
                'client_name': order.client_name,
                'client_phone_number': str(order.client_phone_number),
                'client_email': order.client_email,
                'delivery_address': order.delivery_address,
                'price': order.price,
                'discount': order.discount,
                'total_payable': order.total_payable,
                'status': order.status,
            }
            return JsonResponse(data)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)
        
@csrf_exempt
def update_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(number=order_id)
            order.client_name = request.POST.get('client_name', order.client_name)
            order.client_phone_number = request.POST.get('client_phone_number', order.client_phone_number)
            order.client_email = request.POST.get('client_email', order.client_email)
            order.delivery_address = request.POST.get('delivery_address', order.delivery_address)
            order.price = int(request.POST.get('price', order.price))
            order.discount = int(request.POST.get('discount', order.discount))
            order.total_payable = int(request.POST.get('total_payable', order.total_payable))
            order.status = request.POST.get('status', order.status)

            order.save()
            data = {
                'client_name': order.client_name,
                'client_phone_number': str(order.client_phone_number),
                'client_email': order.client_email,
                'delivery_address': order.delivery_address,
                'price': order.price,
                'discount': order.discount,
                'total_payable': order.total_payable,
            }
            return JsonResponse(data)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)