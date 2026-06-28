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

        request.session["checkout_data"] = {
            "full_name": request.POST["full_name"],
            "phone": request.POST["phone"],
            "house": request.POST["house"],
            "address": request.POST["address"],
            "city": request.POST["city"],
            "state": request.POST["state"],
            "pincode": request.POST["pincode"],
            "total": float(total),
        }

        return redirect("payment")

    return render(request, "orders/checkout.html", {
        "items": items,
        "total": total
    })


@login_required
def payment_choice(request):

    if "checkout_data" not in request.session:
        return redirect("checkout")

    return render(request, "orders/payment_choice.html", {
        "total": request.session["checkout_data"]["total"]
    })


def create_order(request):

    data = request.session.get("checkout_data")

    if not data:
        return

    Order.objects.create(
        user=request.user,
        full_name=data["full_name"],
        phone=data["phone"],
        address=(
            f'{data["house"]}, '
            f'{data["address"]}, '
            f'{data["city"]}, '
            f'{data["state"]} - '
            f'{data["pincode"]}'
        ),
        total_amount=data["total"]
    )

    CartItem.objects.filter(user=request.user).delete()

    del request.session["checkout_data"]


@login_required
def upi_payment(request):

    data = request.session.get("checkout_data")

    if not data:
        return redirect("checkout")

    if request.method == "POST":
        create_order(request)
        return redirect("success")

    return render(request, "orders/upi_payment.html", {
        "total": data["total"]
    })


@login_required
def card_payment(request):

    data = request.session.get("checkout_data")

    if not data:
        return redirect("checkout")

    if request.method == "POST":
        create_order(request)
        return redirect("success")

    return render(request, "orders/card_payment.html", {
        "total": data["total"]
    })


@login_required
def cod_payment(request):

    data = request.session.get("checkout_data")

    if not data:
        return redirect("checkout")

    if request.method == "POST":
        create_order(request)
        return redirect("success")

    return render(request, "orders/cod_payment.html", {
        "total": data["total"]
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
