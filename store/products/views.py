from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.models import Category, Product, Basket


def index(request):
    return render(request, 'products/index.html')

def categories(request):
    categories_list = Category.objects.all()
    context = {'categories': categories_list}
    return render(request, 'products/categories.html', context)

def products(request, category_id, page=1):
    category = Category.objects.get(id=category_id)
    products_by_category = Product.objects.filter(category=category)
    per_page = 3
    paginator = Paginator(products_by_category, per_page)
    products_paginator = paginator.page(page)
    context = {'category': category, 'products': products_paginator}
    return render(request, 'products/products.html', context)

def basket(request):
    return render(request, 'products/basket.html')


def add_product(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user, product=product)
    if not user_baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = user_baskets.last()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTT_REFERER'])

