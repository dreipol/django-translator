# coding=utf-8
from django.core.cache import cache
from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


class Translation(models.Model):
    key = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.key


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        all_translation_keys = Translation.objects.all().values_list('key', flat=True)
        for l in settings.LANGUAGES:
            cache.delete_many(['{0}-{1}'.format(l[0], k) for k in all_translation_keys])
        return super(Translation,self).save(force_insert, force_update, using, update_fields)
