from django.db import models
from .validators import LettersOnlyValidator, PasscodeValidator  # Adjust the import as per your project structure


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[LettersOnlyValidator()],
        help_text="Enter your first name (letters only).",
    )
    last_name = models.CharField(
        max_length=50,
        validators=[LettersOnlyValidator()],
        help_text="Enter your last name (letters only).",
    )
    passcode = models.CharField(
        max_length=6,
        validators=[PasscodeValidator()],
        help_text="Your passcode must be a combination of 6 digits.",
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
