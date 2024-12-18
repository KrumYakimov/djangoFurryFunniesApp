# Generated by Django 5.1.2 on 2024-10-27 07:58

import FurryFunniesApp.authors.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(help_text='Enter your last name (letters only).', max_length=40, validators=[FurryFunniesApp.authors.validators.LettersOnlyValidator()]),
        ),
    ]
