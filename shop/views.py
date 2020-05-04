from django.http import JsonResponse
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

    products_items = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    list_order = list()

    for item in products_items:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['nmb'] = item.nmb
        product_dict['name'] = item.product.name
        product_dict['price'] = item.price_per_item
        list_order.append(product_dict)

    return render(request, 'product/product.html', locals())


