from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    """
    Renders the homepage.

    If a user is authenticated, redirects to the detail page.
    Otherwise, renders the about page.

    Args:
        request: The HTTP request object.

    Returns:
        The HTTP response object.
    """
    return render(request, 'website/about.html')

def detail(request, pk):
    """
    Renders the detail page for a user.

    Args:
        request: The HTTP request object.
        pk: The primary key of the user.

    Returns:
        The HTTP response object.
    """
    user = request.user
    return render(request, 'website/detail.html', {'user': user})

def user_login(request):
    """
    Redirects to the homepage.

    Returns:
        The HTTP redirect response object.
    """
    return redirect('website:home')

def authenticate_user(request):
    """
    Authenticates the user and redirects to their detail page if successful.

    If authentication fails, redirects to the login page with an error message.

    Returns:
        The HTTP redirect response object.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website:detail', pk=user.pk)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('website:login')
    else:
        return redirect('website:login')

def register(request):
    """
    Renders the registration form and processes registration requests.

    If the request method is POST and the form is valid, saves the form data
    and redirects to the login page with a success message.

    Returns:
        The HTTP response object.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('website:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)
