from django.shortcuts import render

from django.shortcuts import render
from .models import Property  # Import your model

def services(request):
    properties = Property.objects.all()
    return render(request, 'properties/services.html', {'properties': properties})
def home(request):
    properties = Property.objects.all()
    return render(request,'index.html')