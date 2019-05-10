# -*- coding: utf-8 -*-
from translator.util import get_translation_for_key


class Translator(object):

    def __init__(self, request):
        self.request = request

    def __getattr__(self, item):
        return get_translation_for_key(item)


def translator(request):
    return {
        'translator': Translator(request)
    }
