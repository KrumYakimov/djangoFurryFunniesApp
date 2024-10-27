from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Post(models.Model):
    MAX_TITLE_LENGTH = 50

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        unique=True,
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        },
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        verbose_name="Post Image URL",
        help_text="Share your funniest furry photo URL!",
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        null=False,
        blank=False,

    )

    author = models.ForeignKey(
        "authors.Author",
        on_delete=models.CASCADE,
        related_name='posts',
        editable=False,
        blank=False,
        null=False,

    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']

