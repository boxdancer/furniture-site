from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

# Если окно войти заполняется через бекенд (у нас в проекте сейчас через html верстку)
# username = forms.CharField(
#     label='Имя',
#     widget=forms.TextInput(attrs={"autofocus": True,
#                                   'class': 'form-control',
#                                   'placeholder': 'Введите ваше имя пользователя', }),
# )
# password = forms.CharField(
#     label='Пароль',
#     widget=forms.PasswordInput(attrs={"autocomplete": 'current-password',
#                                       'class': 'form-control',
#                                       'placeholder': 'Введите ваш пароль', }),
# )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
