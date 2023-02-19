from django.urls import path, include

from .views import categories, products, basket, add_product

urlpatterns = [
    path("", categories, name='categories'),
    path("products/<int:category_id>/", products, name="products"),
    path("page/<int:category_id>/<int:page>", products, name="paginator"),
    path('basket/', basket, name='basket'),
    path('basket/add/<int:product_id>', add_product, name='add_product')
]
