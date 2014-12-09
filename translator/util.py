# -*- coding: utf-8 -*-
from django.utils.functional import lazy
from django.utils.safestring import mark_safe
import hashlib


def get_translation_for_key(item):
    from django.core.exceptions import ObjectDoesNotExist
    from django.utils.translation import get_language
    from translator.models import Translation
    from django.core.cache import cache

    lang = get_language()
    key = get_key(lang, item)
    result = cache.get(key)
    if not result:
        try:
            result = Translation.objects.get(key=item).description
        except ObjectDoesNotExist:
            result = Translation(key=item)
            result.description = item
            result.save()
            result = unicode(result.description)
        cache.set(key, result)
    return mark_safe(result)


def get_key(lang, item):
    item = hashlib.sha256(item).hexdigest()
    key = u'{0}-{1}'.format(lang, item)
    return key

def translator(key):
    return get_translation_for_key(key)


translator_lazy = lazy(get_translation_for_key, unicode)
