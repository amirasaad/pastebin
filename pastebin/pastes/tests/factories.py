from datetime import datetime

from factory import LazyFunction
from factory.django import DjangoModelFactory

from pastebin.pastes.models import Paste


class PasteFactory(DjangoModelFactory):
    created = LazyFunction(datetime.now)

    class Meta:
        model = Paste
