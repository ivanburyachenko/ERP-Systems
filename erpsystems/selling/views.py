from django.shortcuts import render
from base.views import Order
# Create your views here.
def selling(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'selling/selling.html', context)
def order(request, slug):
    order = Order.objects.get(slug=slug)
    context={'order':order}
    return render(request, 'selling/order.html', context)