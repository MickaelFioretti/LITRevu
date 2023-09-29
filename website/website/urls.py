from django.contrib import admin
from django.urls import path
import authentication.views
import flux.views
import ticket.views
import review.views
import post.views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        authentication.views.LoginPageView.as_view(),
        name="login",
    ),
    path("signup", authentication.views.SignupPageView.as_view(), name="signup"),
    path(
        "logout",
        LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path("acceuil/", flux.views.FluxPageView.as_view(), name="acceuil"),
    path(
        "create_ticket/",
        ticket.views.TicketCreatePageView.as_view(),
        name="create_ticket",
    ),
    path(
        "create_review/",
        review.views.ReviewCreatePageView.as_view(),
        name="create_review",
    ),
    path(
        "post/",
        post.views.PostPageView.as_view(),
        name="post",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
