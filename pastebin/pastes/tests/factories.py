from datetime import datetime

from factory import DjangoModelFactory, LazyFunction

from pastebin.pastes.models import Paste


class PasteFactory(DjangoModelFactory):
    created = LazyFunction(datetime.now)

    class Meta:
        model = Paste
