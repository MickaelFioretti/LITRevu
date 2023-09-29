from django.shortcuts import render
from django.views import View
from ticket.models import Ticket
from review.models import Review


# Create your views here.
class PostPageView(View):
    template_name = "post.html"

    def get(self, request):
        tickets = Ticket.objects.all()
        reviews = Review.objects.all()

        # Change the format of the time_created field 13:14, 26 août 2020
        for ticket in tickets:
            ticket.time_created = ticket.time_created.strftime("%H:%M, %d %B %Y")

        for review in reviews:
            review.time_created = review.time_created.strftime("%H:%M, %d %B %Y")
        return render(
            request,
            self.template_name,
            context={"tickets": tickets, "reviews": reviews},
        )
