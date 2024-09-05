from django.shortcuts import render

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