from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here.
class Review(models.Model):
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    time_created = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE)
