# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from translator.models import Translation

CATEGORY_SEPARATOR = getattr(settings, 'DJANGO_TRANSLATOR_CATEGORY_SEPARATOR', '__')


class KeyFilter(admin.SimpleListFilter):
    title = _('Categories')
    parameter_name = 'keys'

    def lookups(self, request, model_admin):
        queryset = model_admin.model.objects.filter(key__contains=CATEGORY_SEPARATOR).values_list('key', flat=True)
        unique_categories = {key.split(CATEGORY_SEPARATOR)[0] for key in queryset}
        categories = sorted([key for key in unique_categories])
        return (
            (category, category) for category in categories
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(key__startswith=self.value())
        else:
            return queryset


class TranslationAdministration(TranslationAdmin):
    list_filter = (KeyFilter, 'tags',)
    search_fields = ['key', 'description', ]
    ordering = ('key',)
    list_display = ('key', 'description',)
    list_editable = ('description',)


admin.site.register(Translation, TranslationAdministration)
