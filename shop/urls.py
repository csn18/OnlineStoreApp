from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='shop'),
    path('product/<int:product_id>', views.product, name='product')
]
