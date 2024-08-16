from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.http import JsonResponse
import stripe

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),  # цена в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'item': item,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'item_detail.html', context)
