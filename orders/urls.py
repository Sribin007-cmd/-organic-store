from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),

    path('payment/', views.payment_choice, name='payment'),

    path('payment/upi/', views.upi_payment, name='upi_payment'),

    path('payment/card/', views.card_payment, name='card_payment'),

    path('payment/cod/', views.cod_payment, name='cod_payment'),

    path('success/', views.success, name='success'),

    path('history/', views.order_history, name='order_history'),
]