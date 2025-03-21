from django.contrib import admin
from .models import House  # Changed from Property


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_by')
    list_filter = ('created_by',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_manager:
            return qs.filter(created_by=request.user)
        return qs


class OrderAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.is_salesperson:  # Salesperson can only approve
            return obj and obj.status == 'pending'
        return super().has_change_permission(request, obj)
