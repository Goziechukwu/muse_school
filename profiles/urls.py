from django.urls import path
from . import views
from .views import instructors_list
from .views import contact_view


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('instructors/', instructors_list, name='instructors_list'),
    path('contact/', contact_view, name='contact'),
]
