from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import stripe
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
def home(request):
    return render(request,'home.html',{})

@csrf_exempt
def create_checkout_session(request):
     
    session = stripe.checkout.Session.create(
                line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/success',
                cancel_url='http://localhost:8000/cancel',
            )
    return redirect(session.url)



def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')