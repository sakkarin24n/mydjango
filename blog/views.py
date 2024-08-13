from django.shortcuts import render
from .models import Product
from django.contrib.humanize.templatetags.humanize import intcomma

def product_list(request):
    products = Product.objects.all()
    for product in products:
        product.formatted_price = intcomma(product.price)
    return render(request, 'product_list.html', {'products': products})

def home(request):
    return render(request, 'home.html')
# Create your views here.
