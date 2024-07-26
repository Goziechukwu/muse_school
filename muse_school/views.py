from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """

    context = {
        'meta_description': ('Page not found - Muse School. Sorry, the page you '
                             'are looking for does not exist.'),
        'title': 'Page Not Found'
    }
    
    return render(request, "errors/404.html", context, status=404)
