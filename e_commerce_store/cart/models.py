from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    phone = models.CharField(
        null=False,
        blank=False,
    )
    address = models.TextField(
        null=False,
        blank=False,
    )

    date = models.DateField(auto_now_add=True)
