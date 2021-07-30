from django.urls import path
from . import views
from .views import *

app_name = 'ACCOUNTS'

urlpatterns = [
    path('Register', Register, name = 'Register'),
    path('Login', Login, name = 'Login'),
    path('Logout', Logout, name = 'Logout'),
    path('', Home, name = 'Home'),
]