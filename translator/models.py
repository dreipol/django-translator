# coding=utf-8
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.utils.decorators import classproperty
from taggit.managers import TaggableManager

from translator.util import get_key


class TranslationBase(models.Model):
    key = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.key

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        all_translation_keys = self.__class__.objects.all().values_list('key', flat=True)
        for l in settings.LANGUAGES:
            cache.delete_many([get_key(l[0], k, self.cache_key_prefix) for k in all_translation_keys])
        return super().save(force_insert, force_update, using, update_fields)

    @classproperty
    def cache_key_prefix(self):
        """To separate cache keys, we need to specify a unique prefix per model."""
        return self._meta.db_table


class Translation(TranslationBase):
    pass
