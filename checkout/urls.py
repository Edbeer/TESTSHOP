from django.urls import path

from .views import *

app_name = 'checkout'

urlpatterns = [
    path('delivery_choices/', delivery_choices, name='delivery_choices'),
    path('basket_update_delivery/', basket_update_delivery, name='basket_update_delivery'),
    path('delivery_address/', delivery_address, name='delivery_address'),
    path('payment_selection/', payment_selection, name='payment_selection'),
    path('payment_complete/', payment_complete, name='payment_complete'),
    path('payment_successful/', payment_successful, name='payment_successful'),
]