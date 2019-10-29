from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Paste(models.Model):
    owner = models.ForeignKey(User, related_name='pastes', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    shared_with = models.ManyToManyField(User, related_name='shared_pastes', blank=True)
    is_public = models.BooleanField(default=True)

