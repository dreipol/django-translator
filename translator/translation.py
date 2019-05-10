# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from translator.models import Translation


class TranslationTranslationOptions(TranslationOptions):
    fields = ('description',)


translator.register(Translation, TranslationTranslationOptions)
