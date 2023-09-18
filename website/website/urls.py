from django.contrib import admin
from django.urls import path
from registration.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', index),
]
