from django.db import models
from django.conf import settings


# Create your models here.
class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_by"
    )

    def __str__(self):
        return f"{self.user.username} suit {self.followed_user.username}"

    class Meta:
        unique_together = ("user", "followed_user")
