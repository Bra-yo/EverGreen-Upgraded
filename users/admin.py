
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('is_manager', 'is_salesperson')
    list_display = ('email', 'is_manager', 'is_salesperson')
