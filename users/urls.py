from django.urls import path
from .views import login, profile, logout,register

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]
