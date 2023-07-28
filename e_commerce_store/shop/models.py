from django.db import models

from e_commerce_store.cart.models import Cart


# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    picture = models.URLField(
        null=False,
        blank=False,
    )

    quantity = models.IntegerField(
        null=False,
        blank=False,
    )

    price = models.IntegerField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
