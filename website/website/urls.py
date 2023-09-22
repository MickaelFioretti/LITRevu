from django.contrib import admin
from django.urls import path
import authentication.views
import flux.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        authentication.views.LoginPageView.as_view(),
        name="login",
    ),
    path("signup", authentication.views.signup_page, name="signup"),
    path(
        "acceuil/",
        flux.views.index,
        name="acceuil"
    )
]
