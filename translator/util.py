# -*- coding: utf-8 -*-
import hashlib
import logging

import six
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError
from django.utils.functional import lazy
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe

from translator.context_processors import DJANGO_TRANSLATOR_MODELS


def get_translation_for_key(item, model_class=None):
    from django.core.exceptions import ObjectDoesNotExist
    from django.utils.translation import get_language
    from translator.models import Translation
    from django.core.cache import cache

    if getattr(settings, "DJANGO_TRANSLATOR_ENABLED", True):
        if not model_class:
            model_class = Translation  # We are using the Translation model as default

        lang = get_language()
        key = get_key(lang, item, model_class.cache_key_prefix)
        result = cache.get(key)

        try:
            if not result:
                try:
                    result = model_class.objects.get(key=item).description
                except ObjectDoesNotExist:
                    result = model_class(key=item)
                    result.description = item
                    result.save()
                    result = result.description
                cache.set(key, result)
        except (OperationalError, ProgrammingError):
            logging.getLogger(__name__).info("Unable to get translation for {0}".format(item), )
            result = item
    else:
        result = item

    return mark_safe(result)


def get_key(lang, item, prefix):
    item = hashlib.sha256(item.encode('utf-8')).hexdigest()
    key = u'{0}-{1}-{2}'.format(lang, prefix, item)
    return key


def translator(key, model_key=None):
    model_class = get_model_class_by_key(model_key=model_key)
    return get_translation_for_key(item=key, model_class=model_class)


def translator_lazy(item, model_key=None):
    if len(item) == 0:
        return ''
    else:
        model_class = get_model_class_by_key(model_key=model_key)
        return lazy(get_translation_for_key, six.text_type)(item=item, model_class=model_class)


def translator_lazy_str(item):
    if len(item) == 0:
        return ''
    else:
        return lazy(get_translation_for_key, str)(item)


def get_model_class_by_key(model_key=None):
    if not model_key:
        return None

    model_class_path = DJANGO_TRANSLATOR_MODELS.get(model_key)
    try:
        return import_string(model_class_path)
    except ImportError:
        return None
