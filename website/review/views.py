from django.shortcuts import render, redirect
from django.views import View
from .models import Review
from django.conf import settings


# Create your views here.
class ReviewCreatePageView(View):
    template_name = "create_review.html"

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        message = ""
        if request.method == "POST":
            headline = request.POST.get("headline")
            body = request.POST.get("body")
            rating = request.POST.get("rating")
            id_ticket = request.POST.get("id_ticket")
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
