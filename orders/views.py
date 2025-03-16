from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from orders.models import Order
from properties.models import Property, House


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def add_to_cart(request, property_id, house_id=None):
    if request.method == 'POST':  # Add method check
        house = get_object_or_404(House, pk=house_id)
        # Check for existing pending order
        if not Order.objects.filter(
            user=request.user,
            property=property,
            status='pending'
        ).exists():
            Order.objects.create(user=request.user, house=house, status='pending')

        return redirect('payment_process')  # Use proper namespace
    return redirect('services')

@login_required
def approve_order(request, order_id):
    if not request.user.is_salesperson:
        return HttpResponseForbidden()
    order = get_object_or_404(Order, id=order_id)
    order.status = 'delivered'
    order.salesperson = request.user
    order.save()
    return redirect('my_orders')
