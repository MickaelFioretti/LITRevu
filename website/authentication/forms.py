from django import forms


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
