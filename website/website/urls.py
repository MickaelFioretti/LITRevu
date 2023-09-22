from django.contrib import admin
from django.urls import path
import authentication.views
import flux.views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        authentication.views.LoginPageView.as_view(),
        name="login",
    ),
    path("signup", authentication.views.signup_page, name="signup"),
    path(
        "logout",
        LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path(
        "acceuil/",
        flux.views.index,
        name="acceuil"
    )
]
