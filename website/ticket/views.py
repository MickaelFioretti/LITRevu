from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from . import forms

# Create your views here.
class TicketCreatePageView(View):
    template_name = "create_ticket.html"
    form_class = forms.TicketForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            context={"form": form}
        )
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        message = ""
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.id_user = request.user
            ticket.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            message = "Veuillez remplir tous les champs."
        return render(
            request,
            self.template_name,
            context={"form": form, "message": message}
        )
