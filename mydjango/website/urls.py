from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

"""
URL pattern for user login.
URL pattern for authenticating user login credentials.
URL pattern for user registration.
URL pattern for displaying user details.
"""

app_name = 'website'
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'), 
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register, name='register'),
    path('detail/<int:pk>/', views.detail, name='detail'),]