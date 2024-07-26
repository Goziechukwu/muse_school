from django.shortcuts import render


# Create your views here.

def index(request):
    """A view to return the index page"""

    context = {
        'meta_description': ('Welcome to Muse School - Innovative Learning '
                             'Solutions for all ages.'),
        'title': 'Home'
    }

    return render(request, 'home/index.html', context)
