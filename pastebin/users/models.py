from django.db.models import CharField

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    name = CharField(_("Name of User"), blank=True, max_length=255)
