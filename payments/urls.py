from django.urls import path
from . import views
from .views import process_payment, mpesa_callback


app_name = 'payments'
urlpatterns = [
    path('process/<int:order_id>/', process_payment, name='process'),
    path('mpesa-callback/', mpesa_callback, name='mpesa_callback'),
]
