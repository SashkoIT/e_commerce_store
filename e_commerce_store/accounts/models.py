from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from e_commerce_store.accounts.validators import letters_only_validator


# Create your models here.

class FruitStoreUser(AbstractUser):
    NAMES_MIN_LENGTH = 2
    NAMES_MAX_LENGTH = 30
    CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show'))

    email = models.EmailField(unique=True)
    first_name = models.CharField(
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
            MaxLengthValidator(NAMES_MAX_LENGTH),
            letters_only_validator,
        )
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
            MaxLengthValidator(NAMES_MAX_LENGTH),
            letters_only_validator,
        )
    )

    gender = models.CharField(
        choices=CHOICES,
        max_length=11,
    )

    profile_picture = models.URLField()

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
