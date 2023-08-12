from django.db import models

from e_commerce_store.accounts.validators import letters_only_validator


# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=(letters_only_validator,)
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    phone = models.CharField(
        blank=False,
        null=False,
        max_length=20,
    )

    subject = models.CharField(
        blank=False,
        null=False,
        max_length=20,
    )

    message = models.TextField(
        blank=False,
        null=False,
    )
