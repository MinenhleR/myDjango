from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'website'
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'), 
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register, name='register'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]