from django.contrib import admin
from django.urls import path, include

from orders.admin import salesperson_admin
from properties import views as properties_views  # Add this import
from orders import views as orders_views
from users import views as users_views
from django.contrib.auth import views as auth_views


# EverGreen/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales-admin/', salesperson_admin.urls),
    path('accounts/', include('allauth.urls')),
    path('services/', properties_views.services, name='services'),
    path('my-orders/', orders_views.my_orders, name='my_orders'),
    path('add-to-cart/<int:property_id>/', orders_views.add_to_cart, name='add_to_cart'),
 path('', users_views.register, name='register'),
    path('login/', users_views.custom_login, name='login'),

    path('payments/', include('payments.urls')),
    path('home/', properties_views.home, name='home'),
    path('about/', users_views.about, name='about'),
    path('contact/', users_views.Contact, name='contact'),
    path('logout/', users_views.custom_logout, name='logout'),

]
