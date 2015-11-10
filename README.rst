===========
Translator
===========

Translator is an app for collecting translations for specified keys in django admin.

Quick start
-----------
#. Install django-translator: ``pip install django-translator``

#. Add "translator, taggit, modeltranslation" to your INSTALLED_APPS setting. Please note that ``modeltranslation`` needs to be before ``django.contrib.admin``:

      INSTALLED_APPS = (
      	  'modeltranslation',
      	  'django.contrib.admin',
           ...
    	  'taggit',
	  'translator',
	  )

#. You have to set the migrations folder for the translator, because we have to add migrations for the set languages.  Add the following to your settings file:
	
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
		    name = models.TextField(verbose_name=_(u"a_key"))

#. Visit the templates. The keys get collected lazy.

#. Translate the keys in the admin.


#. You can disable the translator by setting DJANGO_TRANSLATOR_ENABLED to False.

Project Home
------------
https://github.com/dreipol/django-translator

PyPi
------------
https://pypi.python.org/pypi/django-translator
