
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from cart.models import CartItem


@login_required
def checkout(request):

    items = CartItem.objects.filter(user=request.user)

    if not items.exists():
        return render(request, "cart/empty_cart.html")

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":

        Order.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            phone=request.POST["phone"],
            address=request.POST["address"],
            total_amount=total
        )

        return redirect("payment")

    return render(request, "orders/checkout.html", {
        "items": items,
        "total": total
    })


@login_required
def payment_choice(request):

    items = CartItem.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "orders/payment_choice.html", {
        "items": items,
        "total": total
    })


@login_required
def upi_payment(request):

    items = CartItem.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":
        items.delete()
        return redirect("success")

    return render(request, "orders/upi_payment.html", {
        "total": total
    })


@login_required
def card_payment(request):

    items = CartItem.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":
        items.delete()
        return redirect("success")

    return render(request, "orders/card_payment.html", {
        "total": total
    })


@login_required
def cod_payment(request):

    items = CartItem.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":
        items.delete()
        return redirect("success")

    return render(request, "orders/cod_payment.html", {
        "total": total
    })


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "orders/order_history.html", {
        "orders": orders
    })


def success(request):
    return render(request, "orders/success.html")
