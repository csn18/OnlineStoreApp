from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    country_city = forms.CharField(required=True)
    adr = forms.CharField(required=True)


class OrderInfo(forms.Form):
    phone = forms.IntegerField(required=True)
