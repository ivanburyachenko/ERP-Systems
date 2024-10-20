from django.shortcuts import render
from base.views import Order
# Create your views here.
def selling(request):
    orders = Order.objects.filter(user=request.user)
    statuses = []
    for i in orders:
        if i.status not in statuses:
            statuses.append(i.status)
    context = {'orders':orders, 'statuses': statuses}
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