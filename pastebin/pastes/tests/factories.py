from datetime import datetime

from factory import DjangoModelFactory, Faker, LazyFunction

from pastebin.pastes.models import Paste


class PasteFactory(DjangoModelFactory):
    # content = Faker('content')
    created = LazyFunction(datetime.now)

    class Meta:
        model = Paste
