from django.shortcuts import render, redirect
from django.views import View
from .models import Ticket
from review.models import Review
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# Create your views here.
class TicketCreatePageView(LoginRequiredMixin, View):
    """
    Page de création d'un ticket
    """

    template_name = "create_ticket.html"

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        message = ""
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image = request.FILES.get("image")
            if title and description and image:
                ticket = Ticket.objects.create(
                    title=title,
                    description=description,
                    image=image,
                    id_user=request.user,
                )
                ticket.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Veuillez remplir tous les champs."
        return render(request, self.template_name, context={"message": message})


class TicketDeleteView(LoginRequiredMixin, View):
    """
    Page de suppression d'un ticket
    """

    def post(self, request):
        if request.method == "POST":
            ticket_id = request.POST.get("ticket_id")
            ticket = get_object_or_404(Ticket, id=ticket_id)

            # Supprimez les review liés au ticket
            reviews = Review.objects.filter(id_ticket=ticket)
            for review in reviews:
                review.delete()

            # Supprimez le ticket
            ticket.delete()

            return redirect(settings.LOGIN_REDIRECT_URL)
        return redirect(settings.LOGIN_REDIRECT_URL)


class TicketUpdatePageView(LoginRequiredMixin, View):
    """
    Page de modification d'un ticket
    """

    template_name = "update_ticket.html"

    def get(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        return render(
            request,
            self.template_name,
            context={"ticket": ticket},
        )

    def post(self, request, ticket_id):
        message = ""
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            image = request.FILES.get("image")
            if title and description:
                ticket = get_object_or_404(Ticket, id=ticket_id)
                ticket.title = title
                ticket.description = description
                if image:
                    ticket.image = image
                ticket.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Veuillez remplir tous les champs."
        return render(request, self.template_name, context={"message": message})
