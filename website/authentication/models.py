from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None

    USERNAME_FIELD = 'username'
