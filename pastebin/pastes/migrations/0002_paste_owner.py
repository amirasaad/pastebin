# Generated by Django 2.2.6 on 2019-10-29 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pastes', to=settings.AUTH_USER_MODEL),
        ),
    ]
