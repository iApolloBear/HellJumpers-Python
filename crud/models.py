from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
