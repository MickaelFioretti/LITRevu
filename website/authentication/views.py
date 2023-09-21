from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.conf import settings
from django.views import View

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_URL)
    return render(request, "signup.html", context={"form": form})



class LoginPageView(View):
    template_name = "login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request,
            self.template_name,
            context={"form": form, "message": message}
        )
    

    def post(self, request):
        form = self.form_class(request.POST)
        message = ""
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Nom d'utilisateur ou mot de passe incorrect."
        return render(
            request,
            self.template_name,
            context={"form": form, "message": message}
        )