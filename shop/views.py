from django.shortcuts import render
from shop.models import *
from orders.models import *


def main(request):
    products_images = ProductImg.objects.filter(is_main=True)
    return render(request, 'shop/main_shop.html', locals())


def product(request, product_id):
    products = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'product/product.html', locals())

