from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "headline",
        "id_user",
        "id_ticket",
        "time_created",
    )
    list_filter = ("time_created",)
    search_fields = (
        "headline",
        "id_user__username",
    )
