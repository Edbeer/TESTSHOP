import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51Jr37ZGqJzNCG5PmPMx0yoAnWXklLjpqAJelpZdDJ3Ma4prhHw8zoS4GP84yt50gMhvceHTKBAtUKZlc1TZfR9Nf00Ru3tGgme'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

