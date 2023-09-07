from django.shortcuts import render
from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')
    return render(request, "catalog/contacts.html")


def home(request):
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/product.html', context)
