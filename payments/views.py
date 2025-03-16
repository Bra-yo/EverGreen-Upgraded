import json

from django.shortcuts import render, redirect
from django.shortcuts import render

from orders.models import Order
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Payment
from .mpesa import initiate_stk_push
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        method = request.POST.get('method')
        phone = request.POST.get('phone')  # Add phone field to template

        try:
            if method == 'mpesa':
                response = initiate_stk_push(
                    phone=phone,
                    amount=order.house.price,
                    order_id=order.id
                )

                if 'ResponseCode' in response and response['ResponseCode'] == "0":
                    Payment.objects.create(
                        order=order,
                        method=method,
                        amount=order.house.price,
                        transaction_id=response['CheckoutRequestID']
                    )
                    messages.success(request, "Payment initiated! Complete via MPESA")
                else:
                    messages.error(request, "MPESA payment failed")

            return redirect('my_orders')

        except Exception as e:
            messages.error(request, f"Payment error: {str(e)}")

    return render(request, 'payments/process.html', {
        'order': order,
        'payment_methods': Payment.PAYMENT_METHODS
    })


@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        checkout_id = data['Body']['stkCallback']['CheckoutRequestID']

        payment = Payment.objects.get(transaction_id=checkout_id)
        if data['Body']['stkCallback']['ResultCode'] == 0:
            payment.order.status = 'paid'
            payment.order.save()
            payment.status = 'completed'
            payment.save()

        return JsonResponse({'status': 'received'})
    return JsonResponse({'error': 'Invalid method'}, status=400)