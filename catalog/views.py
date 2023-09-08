from django.shortcuts import render
from catalog.models import Product


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')
    return render(request, "catalog/contacts.html", context)


def home(request):
    products = Product.objects.all()
    context = {
        'object_list': products,
        'title': 'Catalog'
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'object_list': products,
        'title': 'Product'
    }
    return render(request, 'catalog/product.html', context)
