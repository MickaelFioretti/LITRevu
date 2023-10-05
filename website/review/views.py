from django.shortcuts import render, redirect
from django.views import View
from .models import Review
from ticket.models import Ticket
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


# Create your views here.
class ReviewCreatePageView(LoginRequiredMixin, View):
    """
    Page de création d'un review
    """

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


class ReviewDeleteView(LoginRequiredMixin, View):
    """
    Page de suppression d'un review
    """

    def post(self, request):
        if request.method == "POST":
            review_id = request.POST.get("review_id")
            review = get_object_or_404(Review, id=review_id)

            # Supprimez le review
            review.delete()

            return redirect(settings.LOGIN_REDIRECT_URL)
        return redirect(settings.LOGIN_REDIRECT_URL)


class ReviewUpdatePageView(LoginRequiredMixin, View):
    """
    Page de modification d'un review
    """

    template_name = "update_review.html"

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        ticket = get_object_or_404(Ticket, id=review.id_ticket.id)

        return render(
            request,
            self.template_name,
            context={"review": review, "ticket": ticket},
        )

    def post(self, request, review_id):
        message = ""
        if request.method == "POST":
            review = get_object_or_404(Review, id=review_id)

            # Update review
            headline = request.POST.get("headline")
            body = request.POST.get("body")
            rating = request.POST.get("rating")
            if headline and body and rating:
                review.headline = headline
                review.body = body
                review.rating = rating
                review.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Veuillez remplir tous les champs."
        return render(request, self.template_name, context={"message": message})
