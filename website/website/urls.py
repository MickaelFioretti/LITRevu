from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        views.LoginPageView.as_view(),
        name="login",
    ),
    path("signup", views.signup_page, name="signup"),
]
