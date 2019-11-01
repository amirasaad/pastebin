"""
Module: pastebin.pastes.models.

Contains ORM for pastes app.
"""
from django.contrib.auth import get_user_model
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

User = get_user_model()
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Paste(models.Model):
    """Stores all pastes, related to :model:`users.User`."""

    owner = models.ForeignKey(User, related_name='pastes', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    shared_with = models.ManyToManyField(User, related_name='shared_pastes', blank=True)
    is_public = models.BooleanField(default=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):

        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True)
        self.highlighted = highlight(self.content, lexer, formatter)
        super().save(*args, **kwargs)
