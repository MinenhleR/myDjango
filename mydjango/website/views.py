from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'website/about.html')

def detail(request, pk):
    user = request.user
    return render(request, 'website/detail.html', {'user': user})

def user_login(request):
    return redirect('website:home')  

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website:detail', pk=user.pk)  # Redirect to detail view with the user's primary key
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('website:login')
    else:
        return redirect('website:login')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('website:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)