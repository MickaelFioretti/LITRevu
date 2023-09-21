from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from authentication import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),
        name="login",
    ),
    path('admin/', admin.site.urls),
    path('', index),
]
