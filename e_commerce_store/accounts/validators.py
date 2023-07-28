from django.core.exceptions import ValidationError


def letters_only_validator(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError('Name fields must contain only letters!')
