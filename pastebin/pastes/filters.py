import django_filters

from pastebin.pastes.models import Paste


class PasteFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(field_name='created')

    class Meta:
        model = Paste
        fields = ['created']
