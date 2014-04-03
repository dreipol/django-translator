===========
Translator
===========

Translator is an app for collecting translations for specified keys in django admin.

Quick start
-----------

1. Add "translator, taggit, modeltranslation" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
    	  'taggit',
    	  'modeltranslation',
		  'translator',
      )

2. Run ``python manage.py schemamigration translator --auto`` to create the translator models based on the languages you specified in your settings file.

3. Run ``python manage.py migrate`` to migrate the translator models to your database.

4. If you intend to use it in the templates, add 'translator.context_processors.translator' to TEMPLATE_CONTEXT_PROCESSORS ::
	 
	 TEMPLATE_CONTEXT_PROCESSORS = (
	 	...
	    'translator.context_processors.translator',
	 )

5. Create translation keys in your templates and models.
	
	Examples:
	
	Template::
	
		{{ translator.a_key }}
		
	models.py::
	
		from translator.util import translator_lazy as _
		...
		
		class Product(models.Model):
		    name = models.TextField(verbose_name=_(u"a_key"))

6. Visit the templates. The keys get collected lazy.

7. Translate the keys in the admin.