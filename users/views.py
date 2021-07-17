from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import UserRegisterForm, UserProfileForm
from .models import CustomUser


class UserLoginView(LoginView):
    """ Вызывается стандартная форма аутентификации """
    template_name = 'users/login.html'
    # не работает
    # authentication_form = UserLoginForm  # возможно это тоже лишнее
    # extra_context = {'myform': UserLoginForm}


class UserLogoutView(LogoutView):
    pass


class UserProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    # как сделать редирект с <int:pk>?
    success_url = reverse_lazy('bboard:index')
    form_class = UserProfileForm

    def form_valid(self, form):
        messages.success(self.request, 'Изменения сохранены')
        return super().form_valid(form)


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('bboard:index')
    template_name = 'users/password_change.html'

    def form_valid(self, form):
        messages.success(self.request, 'Пароль изменен')
        return super().form_valid(form)


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm

    def form_valid(self, form):
        messages.success(self.request, 'Регистрация прошла успешно. Авторизуйтесь')
        return super().form_valid(form)
