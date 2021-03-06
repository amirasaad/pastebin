# Generated by Django 2.2.6 on 2019-10-29 21:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pastes", "0002_paste_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="paste",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="paste",
            name="shared_with",
            field=models.ManyToManyField(
                related_name="shared_with", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
