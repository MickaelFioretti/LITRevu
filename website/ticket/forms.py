from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                "placeholder": "Titre",
            }
        ),
    )
    description = forms.CharField(
        max_length=2048,
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 mb-2 border border-slate-600 rounded-lg font-medium",
                "placeholder": "Description",
            }
        ),
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "",
                "placeholder": "Image",
            }
        ),
    )

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
