from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView,UserProfileView,UserPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/password/', UserPasswordChangeView.as_view(), name='password_change'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
