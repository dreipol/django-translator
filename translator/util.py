# -*- coding: utf-8 -*-
from django.utils.functional import lazy
from django.utils.safestring import mark_safe
from django.db.utils import OperationalError
import hashlib
import logging


def get_translation_for_key(item):
    from django.core.exceptions import ObjectDoesNotExist
    from django.utils.translation import get_language
    from translator.models import Translation
    from django.core.cache import cache

    lang = get_language()
    key = get_key(lang, item)
    result = cache.get(key)

    try:
        if not result:
            try:
                result = Translation.objects.get(key=item).description
            except ObjectDoesNotExist:
                result = Translation(key=item)
                result.description = item
                result.save()
                result = result.description
            cache.set(key, result)
    except OperationalError:
        logging.getLogger(__name__).info("Unable to get translation for {0}".format(item), )
        result = item

    return mark_safe(result)


def get_key(lang, item):
    item = hashlib.sha256(item.encode('utf-8')).hexdigest()
    key = u'{0}-{1}'.format(lang, item)
    return key

def translator(key):
    return get_translation_for_key(key)


translator_lazy = lazy(get_translation_for_key, str)
