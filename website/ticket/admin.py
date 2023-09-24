from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_user', 'time_created')  # Champs à afficher dans la liste
    list_filter = ('time_created',)  # Filtre par date de création
    search_fields = ('title', 'id_user__username')  # Recherche par titre et nom d'utilisateur
