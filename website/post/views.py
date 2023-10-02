from django.shortcuts import render
from django.views import View
from ticket.models import Ticket
from review.models import Review
from datetime import datetime


# Create your views here.
class PostPageView(View):
    template_name = "post.html"

    def get(self, request):
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()
        message = ""

        # Change the format of the time_created field 13:14, 26 août 2020
        for ticket in tickets:
            ticket.time_created = datetime.strptime(
                ticket.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
            )

        for review in reviews:
            review.time_created = datetime.strptime(
                review.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
            )
            review.rating_empty = range(5 - review.rating)
            review.rating = range(review.rating)

        # si ticket et vide print message
        if not tickets and not reviews:
            message = "Il n'y a pas de ticket ou de review pour le moment"

        return render(
            request,
            self.template_name,
            context={
                "tickets": tickets,
                "reviews": reviews,
                "user": request.user,
                "message": message,
            },
        )
