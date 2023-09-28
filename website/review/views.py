from django.shortcuts import render, redirect
from django.views import View
from .models import Review
from ticket.models import Ticket
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ReviewCreatePageView(LoginRequiredMixin, View):
    template_name = "create_review.html"

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        message = ""
        if request.method == "POST":
            # Create ticket
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
            else:
                message = "Veuillez remplir tous les champs."

            # Create review
            headline = request.POST.get("headline")
            body = request.POST.get("body")
            rating = request.POST.get("rating")
            id_ticket = ticket
            if headline and body and rating and id_ticket:
                review = Review.objects.create(
                    headline=headline,
                    body=body,
                    rating=rating,
                    id_user=request.user,
                    id_ticket=id_ticket,
                )
                review.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Veuillez remplir tous les champs."
        return render(request, self.template_name, context={"message": message})
