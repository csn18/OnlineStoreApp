from django.shortcuts import render
from shop.models import ProductImg


def main(request):

    products_images = ProductImg.objects.filter(is_main=True)[:3]

    return render(request, 'home/main_home.html', locals())
