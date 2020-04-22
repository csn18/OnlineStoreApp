from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='order'),
    path('basket/', views.basket, name='basket')
]
