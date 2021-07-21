from django.urls import path
from . import views
from .views import *

app_name = 'ACCOUNTS'

urlpatterns = [
    path('', Register, name = 'Register'),
    path('Login', Login, name = 'Login'),
    path('Logout', Logout, name = 'Logout'),
    path('Home', Home, name = 'Home'),
    path('About', About, name = 'About'),
]