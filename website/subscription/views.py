from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserFollows
from authentication.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


# Create your views here.
class SubscriptionPageView(LoginRequiredMixin, View):
    """
    Page pour gerer les abonnements
    """

    template_name = "subscription.html"

    def get(self, request):
        # Récupérez les abonnements de l'utilisateur actuel
        abonnements = UserFollows.objects.filter(user=request.user)
        # Récupérez les abonnés de l'utilisateur actuel
        abonnes = UserFollows.objects.filter(followed_user=request.user)

        return render(
            request,
            self.template_name,
            context={
                "abonnements": abonnements,
                "abonnes": abonnes,
            },
        )

    def post(self, request):
        action = request.POST.get("action")

        if action:
            if action == "follow":
                # Vérifiez si l'utilisateur existe et n'est pas déjà suivi
                username = request.POST.get("username")
                user_id = get_object_or_404(User, username=username).id
                if not UserFollows.objects.filter(
                    user=request.user, followed_user=user_id
                ).exists():
                    abonnement = UserFollows.objects.create(
                        user=request.user,
                        followed_user=get_object_or_404(User, id=user_id),
                    )
                    abonnement.save()
            elif action == "unfollow":
                # Vérifiez si l'utilisateur existe et est suivi
                user_id = request.POST.get("user_id")
                abonnement = UserFollows.objects.filter(
                    user=request.user,
                    followed_user=get_object_or_404(User, id=user_id),
                )
                abonnement.delete()
            else:
                return render(
                    request,
                    self.template_name,
                    context={"message": "Action non reconnue."},
                )

        return redirect("abonnements")
