from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.conf import settings
from django.views import View
from .models import User

from . import forms


class SignupPageView(View):
    template_name = "signup.html"

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        message = ""
        if request.method == "POST":
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if username and password1 and password2:
                if password1 == password2:
                    user = User.objects.create_user(
                        username=username, password=password1
                    )
                    user.save()
                    return redirect(settings.LOGIN_URL)
                else:
                    message = "Les mots de passe ne correspondent pas."
            else:
                message = "Veuillez remplir tous les champs."
        return render(
            request,
            self.template_name,
            context={"message": message},
        )


class LoginPageView(View):
    template_name = "login.html"
    form_class = forms.LoginForm

    def get(self, request):
        message = ""
        return render(
            request, self.template_name, context={"message": message}
        )

    def post(self, request):
        message = ""
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Nom d'utilisateur ou mot de passe incorrect."
        return render(
            request, self.template_name, context={"message": message}
        )
