from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from .models import Product


def checkout(request):
    # Get product ID from query parameters
    product_id = request.GET.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        messages.error(request, "The product you're trying to purchase does not exist")
        return redirect(reverse('products'))

    order_form = OrderForm()

    # Calculate totals
    product_price = product.price
    delivery = 0  # No delivery cost for digital products
    grand_total = product_price + delivery

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'product': product,
        'total': product_price,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, template, context)
