from django.http import JsonResponse
from django.shortcuts import render

from .models import ProductInBasket


def main(request):
    return render(request, 'order/main_order.html')


def basket(request):
    return_dict = dict()

    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                 defaults={"nmb": nmb})
    if not created:
        print("not created")
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)

    products_items = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_nmb = products_items.count()
    return_dict['total_nmb'] = product_total_nmb
    return_dict['products'] = list()

    for item in products_items:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['nmb'] = item.nmb
        product_dict['name'] = item.product.name
        product_dict['price'] = item.price_per_item
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)
