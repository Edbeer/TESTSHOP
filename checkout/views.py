from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import DeliveryOptions


@login_required
def delivery_choices(request):
    delivery_options = DeliveryOptions.objects.filter(is_active=True)
    return render(request, 'checkout/delivery_choices.html', {'delivery_options': delivery_options})
