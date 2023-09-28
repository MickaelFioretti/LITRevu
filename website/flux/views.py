from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class FluxPageView(LoginRequiredMixin, View):
    template_name = "flux.html"

    def get(self, request):
        return render(request, self.template_name, context={})
