from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from .models import CustomUser


# не нужно, пока не решишь вопрос со сменой формы аутентификации
# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password', 'phone')


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone')


# * - ReadOnlyPasswordHashWidget и ReadOnlyPasswordHashField
# Весь код в * только для того, чтобы убрать строку "No password set."
# ReadOnlyPasswordHashField обязателен, иначе изменения не применятся
# ReadOnlyPasswordHashWidget и ReadOnlyPasswordHashField должны быть выше UserProfileForm
class ReadOnlyPasswordHashWidget(forms.Widget):
    template_name = 'auth/widgets/read_only_password_hash.html'
    read_only = True

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        summary = []
        if not value or value.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary.append({'label': gettext("")})  # вот тут изменил gettext("No password set.")
        else:
            try:
                hasher = identify_hasher(value)
            except ValueError:
                summary.append({'label': gettext("Invalid password format or unknown hashing algorithm.")})
            else:
                for key, value_ in hasher.safe_summary(value).items():
                    summary.append({'label': gettext(key), 'value': value_})
        context['summary'] = summary
        return context


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        kwargs.setdefault('disabled', True)
        super().__init__(*args, **kwargs)


class UserProfileForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Raw passwords are not stored, so there is no way to see this '
            'user’s password, but you can change the password using '
            '<a href="{}">this form</a>.'),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone')
