from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from subscription.models import UserFollows
from ticket.models import Ticket
from review.models import Review
from itertools import chain
from datetime import datetime


class FluxPageView(LoginRequiredMixin, View):
    template_name = "flux.html"

    def get(self, request):
        # get all followed users
        followed_users = UserFollows.objects.filter(user=request.user.id)

        # get all tickets and reviews from the followed users
        tickets = []
        reviews = []

        for followed_user in followed_users:
            # Get all ticket from the followed users
            user_tickets = Ticket.objects.filter(id_user=followed_user.followed_user.id)
            # Get all reviews from the followed users
            user_reviews = Review.objects.filter(id_user=followed_user.followed_user.id)

            # Ajoutez le type de poste aux billets et critiques
            for ticket in user_tickets:
                ticket.post_type = "Ticket"
                ticket.time_created = datetime.strptime(
                    ticket.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
                )
            for review in user_reviews:
                review.post_type = "Review"
                review.time_created = datetime.strptime(
                    review.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
                )
                review.rating_empty = range(5 - review.rating)
                review.rating = range(review.rating)

            # Ajoutez les billets et les critiques à leurs listes respectives
            tickets.extend(user_tickets)
            reviews.extend(user_reviews)

        # Get your own tickets and reviews
        your_tickets = Ticket.objects.filter(id_user=request.user)
        your_reviews = Review.objects.filter(id_user=request.user)

        # Récupérez les réponses aux billets de l'utilisateur connecté
        your_ticket_responses = Review.objects.filter(id_ticket__id_user=request.user)

        for ticket in your_tickets:
            ticket.post_type = "Ticket"
            ticket.time_created = datetime.strptime(
                ticket.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
            )

        for review in your_reviews:
            review.post_type = "Review"
            review.time_created = datetime.strptime(
                review.time_created.strftime("%H:%M, %d %B %Y"), "%H:%M, %d %B %Y"
            )
            review.rating_empty = range(5 - review.rating)
            review.rating = range(review.rating)

        for ticket_response in your_ticket_responses:
            ticket_response.post_type = "Review"
            ticket_response.time_created = datetime.strptime(
                ticket_response.time_created.strftime("%H:%M, %d %B %Y"),
                "%H:%M, %d %B %Y",
            )
            ticket_response.rating_empty = range(5 - ticket_response.rating)
            ticket_response.rating = range(ticket_response.rating)

        # Add your own tickets and reviews to their respective lists
        tickets.extend(your_tickets)
        reviews.extend(your_reviews)

        # Add ticket responses to the list
        reviews.extend(your_ticket_responses)

        # combine and sort tickets and reviews
        posts = sorted(
            chain(tickets, reviews), key=lambda post: post.time_created, reverse=True
        )
        return render(
            request, self.template_name, context={"posts": posts, "tickets": tickets}
        )
