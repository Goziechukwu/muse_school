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
        'stripe_public_key': 'pk_test_51PLhJV05uNCTQMdd9eDBB5gLawJqNitalgVk7PN9staen9hfNb0ENrXo5JxqWuVXcs6jnhigEPomAG2rjS0XHWLn00eCEc50cp',
        'client_secret': 'test client secret',
        'product': product,
        'total': product_price,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, template, context)
