from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile  # Changed from CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile  # Update model reference
        fields = ('email', 'username', 'phone')  # Add custom fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile  # Update model reference
        fields = ('email', 'username', 'phone', 'is_manager', 'is_salesperson')