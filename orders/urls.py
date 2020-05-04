from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('info/', views.info, name='info'),
    path('', views.checkout, name='orders'),
]
