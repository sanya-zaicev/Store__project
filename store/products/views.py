from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import Category, Product, Basket

class MainView(TemplateView):
    template_name = 'products/index.html'

def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {'baskets':baskets}
    return render(request, 'products/basket.html', context)

def add_product(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user, product=product)

    if not user_baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = user_baskets.last()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    user_baskets = Basket.objects.filter(user=request.user, product=product)
    basket = user_baskets.last()
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def delete_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class CategoriesListView(ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 6

class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        return queryset.filter(category=category)

