import datetime
from logging import PlaceHolder
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, TextInput, widgets
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Логин или почта"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Пароль"}
        )
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Логин"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Пароль"}
        ),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Повтор пароля"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "last_name",
            "first_name",
            "email",
            "username",
            "password1",
            "password2",
        )
        labels = {"first_name": "Имя", "last_name": "Фамилия", "email": "E-mail"}
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Имя"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Фамилия"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "E-mail"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Данный E-mail уже занят")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True, widget=TextInput(attrs={"class": "form-input"}), label="Логин"
    )
    email = forms.CharField(
        disabled=True, widget=TextInput(attrs={"class": "form-input"}), label="E-mail"
    )
    this_year = datetime.date.today().year
    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            years=tuple(range(this_year - 100, this_year + 1)),
            attrs={"class": "date-select"},
        )
    )

    class Meta:
        model = get_user_model()
        fields = (
            "last_name",
            "first_name",
            "date_birth",
            "email",
            "username",
        )
        labels = {"first_name": "Имя", "last_name": "Фамилия"}
        widgets = {
            "first_name": TextInput(attrs={"class": "form-input"}),
            "last_name": TextInput(attrs={"class": "form-input"}),
        }


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "E-mail",
            }
        ),
    )


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Новый пароль",
            }
        ),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Повторите новый пароль",
            }
        ),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Старый пароль"}
        )
    )
    new_password1 = CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Новый пароль"}
        )
    )
    new_password2 = CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Новый пароль ещё раз"}
        )
    )
