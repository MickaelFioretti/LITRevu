from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                    "placeholder": "Nom d'utilisateur",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                    "placeholder": "Mot de passe",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                    "placeholder": "Confirmation du mot de passe",
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                "placeholder": "Nom d'utilisateur",
            }
        ),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                "placeholder": "Mot de passe",
            }
        ),
    )