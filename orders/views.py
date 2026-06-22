from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order
from cart.models import CartItem
from django.shortcuts import render, redirect

def payment(request):

    if request.method == 'POST':
        return redirect('success')

    return render(request, 'orders/payment.html')


def success(request):
    return render(request, 'orders/success.html')


@login_required
def checkout(request):

    items = CartItem.objects.filter(user=request.user)

    # Prevent checkout if cart is empty
    if not items.exists():
        return render(
            request,
            'cart/empty_cart.html'
        )

    total = 0

    for item in items:
        total += item.product.price * item.quantity
    

    for item in items:
        total += item.product.price * item.quantity

    if request.method == 'POST':

        Order.objects.create(
            user=request.user,
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            total_amount=total
        )

        items.delete()

        return render(
            request,
            'orders/success.html'
        )

    return render(
        request,
        'orders/checkout.html',
        {
            'items': items,
            'total': total
        }
    )


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )