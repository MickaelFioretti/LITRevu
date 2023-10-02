from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "input-text",
                "placeholder": "Nom d'utilisateur",
            }
        ),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(
            attrs={
                "class": "input-password",
                "placeholder": "*********",
            }
        ),
    )
