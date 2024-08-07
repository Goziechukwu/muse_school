from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from .forms import ContactRequestForm

from .models import Instructor

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'meta_description': ('Manage your profile and account settings at '
                             'Muse School.'),
        'title': 'Profile'
    }

    return render(request, template, context)


def instructors_list(request):
    """
    Display the list of Instructors
    """
    instructors = Instructor.objects.all()
    return render(request, 'profiles/instructors_list.html', {'instructors': instructors})


def contact_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactRequestForm()
    return render(request, 'profiles/contact.html', {'form': form})


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
