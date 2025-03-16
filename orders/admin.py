
# orders/admin.py
from django.contrib import admin
from .models import Order

class SalespersonAdminSite(admin.AdminSite):
    class SalespersonAdminSite(admin.AdminSite):
        def has_permission(self, request):
            return request.user.is_active and request.user.is_salesperson  # New
    site_header = "Salesperson Portal"
    site_title = "EverGreen Sales Portal"

class ManagerAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_manager
    site_header = "Manager Portal"
    site_title = "EverGreen Management"

# Instantiate the custom admin sites
salesperson_admin = SalespersonAdminSite(name='salesperson_admin')
manager_admin = ManagerAdminSite(name='manager_admin')

# Register models with custom admin site
@admin.register(Order, site=salesperson_admin)
class SalespersonOrderAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_salesperson:
            return qs.filter(status='pending')
        return qs


    list_display = ['user', 'house', 'status', 'created_at']  # Added date
    list_filter = ['status']




@admin.register(Order, site=manager_admin)
class ManagerOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'house', 'status', 'salesperson']

admin.site.register(Order, ManagerOrderAdmin)
