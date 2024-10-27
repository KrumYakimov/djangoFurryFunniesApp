from django.db import models
from .validators import LettersOnlyValidator, PasscodeValidator  # Adjust the import as per your project structure


class Author(models.Model):
    MAX_FIRST_NAME_LENGTH = 40
    MAX_LAST_NAME_LENGTH = 40
    MAX_PASSCODE_LENGTH = 6

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[LettersOnlyValidator()],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[LettersOnlyValidator()],
        blank=False,
        null=False,
    )

    passcode = models.CharField(
        max_length=MAX_PASSCODE_LENGTH,
        validators=[PasscodeValidator()],
        blank=False,
        null=False,
    )

    pets_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )

    info = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
