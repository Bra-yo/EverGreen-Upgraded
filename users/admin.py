from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .forms import CustomUserChangeForm

@admin.register(UserProfile)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'phone', 'is_manager', 'is_salesperson')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone', 'is_manager', 'is_salesperson')}),
    )