from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product
# from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # return HttpResponse("Hello World")
    x = calculate()
    # y = 2
    return render(request, 'hello.html', { 'name': 'Joey' })

def test_query(request):
    products = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price__lt=20)
    ).order_by('title')

    return render(request, 'hello.html', { 'name': 'Joey', 'products': list(products) })