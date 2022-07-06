from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Producer, Category

def index(request):

    producers = Producer.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    data = {
        'categories': categories,
        'producers': producers,
        'products': products,
            }
    return render(request, 'main.html', data)

def categories(request, id):

    category_select = Category.objects.get(pk=id)
    products = Product.objects.filter(category=category_select)
    categories = Category.objects.all()

    data = {
        'category_select': category_select,
        'products': products,
        'categories': categories
            }
    return render(request, 'categories_products.html', data)




