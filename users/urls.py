from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserProfileView, UserPasswordChangeView, activate

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<slug:slug>/', UserProfileView.as_view(), name='profile'),
    path('profile/password/', UserPasswordChangeView.as_view(), name='password_change'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('activate/<str:activation_key>', activate, name='activate'),
]
