from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ImagesConfig(AppConfig):
    name = 'wiki.plugins.images'
    verbose_name = _("Wiki images")
    label = 'wiki_images'