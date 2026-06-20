from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.product_list,
        name='product_list'
    ),

    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        '<int:product_id>/review/',
        views.add_review,
        name='add_review'
    ),

]