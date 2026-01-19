from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Define a simple username and password for authentication
USERNAME = 'user'
PASSWORD = 'password'

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == USERNAME and password == PASSWORD:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse("Invalid credentials")
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')