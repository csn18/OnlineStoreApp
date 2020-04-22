from .models import ProductInBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_items = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_nmb = products_items.count()

    return locals()
