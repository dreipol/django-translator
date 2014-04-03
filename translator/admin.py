# -*- coding: utf-8 -*-
from django.contrib import admin
from translator.models import Translation
from modeltranslation.admin import TranslationAdmin


class TranslationAdministration(TranslationAdmin):
    list_filter = ('tags',)
    search_fields = ['key', 'description',]
    ordering = ('key',)
    list_display = ('key', 'description',)
    list_editable = ('description',)


admin.site.register(Translation, TranslationAdministration)
