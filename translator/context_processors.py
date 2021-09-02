# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.module_loading import import_string

DJANGO_TRANSLATOR_MODELS = getattr(settings, 'DJANGO_TRANSLATOR_MODELS', {})


class Translator(object):

    def __init__(self, request, model_class=None):
        from translator.models import Translation

        self.request = request
        self.model_class = model_class or Translation

    def __getattr__(self, item):
        from translator.util import get_translation_for_key

        return get_translation_for_key(item=item, model_class=self.model_class)


def translator(request):
    context = {'translator': Translator(request)}
    for variable_name, model_class_path in DJANGO_TRANSLATOR_MODELS.items():
        model_class = import_string(model_class_path)
        context[variable_name] = Translator(request, model_class)
    return context
