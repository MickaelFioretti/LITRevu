from django.shortcuts import render, redirect
from django.views import View
from .models import Ticket
from django.conf import settings



# Create your views here.
class TicketCreatePageView(View):
    template_name = "create_ticket.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={}
        )
    
    def post(self, request):
        message = ""
        print("*" * 100, request)
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image = request.FILES.get("image")
            if title and description and image:
                ticket = Ticket.objects.create(
                    title=title,
                    description=description,
                    image=image,
                    id_user=request.user
                )
                ticket.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Veuillez remplir tous les champs."
        return render(
            request,
            self.template_name,
            context={"message": message}
        )