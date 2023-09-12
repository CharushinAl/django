from django.shortcuts import render, get_object_or_404
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
    context = {
        'object_list': Product.objects.all(),
        'title': 'Catalog'
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Product'
    }
    return render(request, 'catalog/product.html', context)


def product_detail(request, product_id: int):
    context = {
        'object_list': Product.objects.filter(product_id=product_id),
        'title': 'Product'
    }
    return render(request, 'catalog/product.html', context)
