===========
Translator
===========

Translator is an app for collecting translations for specified keys in django admin.

Quick start
-----------
#. Install django-translator: ``pip install django-translator``

#. Add "translator, taggit, modeltranslation" to your INSTALLED_APPS setting. Please note that ``modeltranslation`` needs to be before ``django.contrib.admin``::

	INSTALLED_APPS = (
	'modeltranslation',
	'django.contrib.admin',
	...
	'taggit',
	'translator',
	)

#. You have to set the migrations folder for the translator, because we have to add migrations for the set languages.  Add the following to your settings file::

	MIGRATION_MODULES = {
	    'translator': 'my_project.translator_migrations',
	}

#. Create a ``translator_migrations`` python package in your project folder (where your settings.py usually is).

#. Run ``python manage.py makemigrations translator`` to create the translator models based on the languages you specified in your settings file.

#. Run ``python manage.py migrate`` to migrate the translator models to your database.

#. If you intend to use it in the templates, add 'translator.context_processors.translator' to TEMPLATE_CONTEXT_PROCESSORS ::

	 TEMPLATE_CONTEXT_PROCESSORS = (
	 	...
	    'translator.context_processors.translator',
	 )

#. Create translation keys in your templates and models.

	Examples:

	Template::

		{{ translator.a_key }}

	models.py::

		from translator.util import translator_lazy as _
		...

		class Product(models.Model):
		    name = models.TextField(verbose_name=_('a_key'))

#. Visit the templates. The keys get collected lazy.

#. Translate the keys in the admin.


#. You can disable the translator by setting DJANGO_TRANSLATOR_ENABLED to False.

#. Use a double underscore in your translation keys to make use of the filter in the admin (e.g. "header__title" creates a filter called "header"). If you need another separator, set it as DJANGO_TRANSLATOR_CATEGORY_SEPARATOR in your setting file.


Custom Models
-------------

If you find yourself in a situation where you need to use the features of django-translator in a second isolated model, feel free to add one:

#. Create a new model in your app::

    from translator.models import TranslationBase

    class MyCustomTranslation(TranslationBase):
        pass


#. Create a new file `translation.py` and register your model for modeltranslation support::

    from modeltranslation.translator import translator, TranslationOptions
    from myapp.models import MyCustomTranslation

    class MyCustomTranslationOptions(TranslationOptions):
        fields = ('description',)

    translator.register(MyCustomTranslation, MyCustomTranslationOptions)


#. Add a django admin in `admin.py`::

    from django.contrib import admin
    from translator.admin import TranslationAdministration
    from myapp.models import MyCustomTranslation

    @admin.register(MyCustomTranslation)
    class CustomTranslationAdmin(TranslationAdministration):
        pass


#. Add your model to your settings file::

    DJANGO_TRANSLATOR_MODELS = {
        'custom_translation': 'myapp.models.MyCustomTranslation',
    }


#. Create translation keys in your templates and models.

	Examples:

	Template::

		{{ custom_translation.a_key }}

	models.py::

		from myapp.util import custom_translation_lazy
		...

		class Product(models.Model):
		    name = models.TextField(verbose_name=translator_lazy('a_key', 'custom_translation'))

Settings
-------------
Customize the translator in your settings.py file with these settings::

	DJANGO_TRANSLATOR_CACHE_TIMEOUT = timeout in seconds, if not set defaults to DEFAULT_TIMEOUT, which is either the CACHES['TIMEOUT'] setting or 300 (5 minutes)


Project Home
------------
https://github.com/dreipol/django-translator

PyPi
------------
https://pypi.python.org/pypi/django-translator
