from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from pyexpat.errors import messages
from django.http import HttpResponse


from .models import CustomUser




from .forms import CustomUserCreationForm  # Import your custom form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use custom form
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('home')
            # Add your success logic
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

import logging
logger = logging.getLogger(__name__)


def custom_login(request):
    logger.debug("Login view called")

    if request.method == 'POST':
        logger.debug("POST request received")

        # Get username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        logger.debug(f"Attempting to authenticate user: {username}")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            logger.debug("User authenticated successfully")
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            logger.debug("Authentication failed")
            # Return the login page with an error message
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})

    # Handle GET requests (display the login form)
    logger.debug("GET request received")
    return render(request, 'registration/login.html')

