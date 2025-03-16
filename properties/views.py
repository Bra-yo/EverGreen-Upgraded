from django.shortcuts import render
from .models import House  # Changed from Property

def services(request):
    houses = House.objects.all()
    return render(request, 'properties/services.html', {'houses': houses})

def home(request):
    houses = House.objects.all()
    return render(request, 'index.html', {'houses': houses})