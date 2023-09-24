from django.db import models
from django.conf import settings

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(upload_to='tickets/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title