# coding=utf-8
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.utils.functional import classproperty

from translator.util import get_key


class TranslationBase(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.key

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        for language_code, _ in settings.LANGUAGES:
            cache.delete(get_key(language_code, self.key, self.cache_key_prefix))
        return super().save(force_insert, force_update, using, update_fields)

    @classproperty
    def cache_key_prefix(self):
        """To separate cache keys, we need to specify a unique prefix per model."""
        return self._meta.db_table


class Translation(TranslationBase):
    pass
