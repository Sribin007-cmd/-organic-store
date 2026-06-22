from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),


    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'history/',
        views.order_history,
        name='order_history'
    ),

]