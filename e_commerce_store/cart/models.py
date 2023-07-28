from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
