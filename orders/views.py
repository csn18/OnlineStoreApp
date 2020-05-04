from django.http import JsonResponse
from django.shortcuts import render

from .forms import *
from .models import *


def basket(request):
    return_dict = dict()

    session_key = request.session.session_key
    data = request.POST
    product_id = data['product_id']
    nmb = data['nmb']

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                 defaults={"nmb": nmb})
    if not created:
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
        product_dict['price'] = int(item.price_per_item)
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)

    if request.POST:
        if request.POST.get('is_delete'):
            id_element = request.POST['id']
            ProductInBasket.objects.filter(id=id_element).delete()
        elif form.is_valid():
            print(request.POST)
            data = request.POST
            name = data['first_name']
            phone = data['phone']
            email = data['email']
            customer_address = data['country_city'] + ' ' + data['adr']
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone,
                                         customer_address=customer_address, customer_email=email, status_id=1)

            for name, value in data.items():
                if name.startswith('product_in_basket_'):
                    product_in_basket_id = name.split('product_in_basket_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product,
                                                  nmb=product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

                    ProductInBasket.objects.filter(id=product_in_basket_id).delete()

        else:
            print('NO')
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return render(request, 'orders/orders.html', locals())


def info(request):
    session_key = request.session.session_key
    print(request.POST)

    if request.POST:
        phone = request.POST['phone_number']
        print(phone)
        data = Order.objects.filter(customer_phone=phone)
        data_list = list()
        for item in data:
            product_dict = dict()
            product_dict['id'] = item.id
            product_dict['name'] = item.customer_name
            product_dict['email'] = item.customer_email
            product_dict['phone'] = item.customer_phone
            product_dict['address'] = item.customer_address
            product_dict['status'] = str(item.status)
            product_dict['total_price'] = str(item.total_price)
            product_dict['created_date'] = str(item.created)
            data_list.append(product_dict)

        print(data_list)
        return JsonResponse(data_list, safe=False)

    return render(request, 'orders/info.html', locals())
