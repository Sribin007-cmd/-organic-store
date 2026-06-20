from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Review
from .forms import ReviewForm


def product_list(request):

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            name__icontains=query
        )
    else:
        products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {
            'products': products
        }
    )


def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    recommendations = Product.objects.exclude(
        id=product.id
    )[:4]

    reviews = Review.objects.filter(
        product=product
    ).order_by('-created_at')

    form = ReviewForm()

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product,
            'recommendations': recommendations,
            'reviews': reviews,
            'form': form
        }
    )


@login_required
def add_review(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(
                commit=False
            )

            review.product = product

            review.user = request.user

            review.save()

    return redirect(
        'product_detail',
        product_id=product.id
    )