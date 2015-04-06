===========
DJANGO-SKIN
===========

Adds the ability to add "skins" to django projects by adding a custom template loader. This is useful if you have a
single code base with multiple deployments

*************
Documentation
*************

Add to ``INSTALLED APPS``
=========================
    Add the module to your installed apps.

    .. code-block:: python

        INSTALLED_APS = (
            ...
            'skin'
        )

Use a skin
==========

There are two different ways you can use skins with django-skin. Using the new template loaders will add skins
globally to any Template views. Using the new `TemplateSkinView` will allow you to explicitly add a skin to a
specific views.

Template Loader
---------------
    Add either of the template loaders to the top of your ``TEMPLATE_LOADERS`` in settings.py

    .. code-block:: python

        TEMPLATE_LOADERS = (
            'skin.template.loaders.filesystem.Loader',
            'skin.template.loaders.app_directories.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )

Custom View
-----------
    You can also just use the `TemplateSkinView` to allow only specific views to be skinned.

    .. code-block:: python

        from skin.views import TemplateSkinView

        class YourView(TemplateSkinView):
            template_name = 'yourview.html'

            def get(self, request, **kwargs):
                # Your view code

    You can also set two different attributes when using this view to overwrite the skin.

    * *skin_name:* setting this will override what is in settings.SKIN_NAME
    * *skin_path:* setting this will specify the exact path and will cause the view to ignore `skin_name` and any
    created `SiteSkin`s.

Run migrations
==============
    If you have south, run migrations

    .. code-block:: bash

        $ python manage.py migrate skin

Create skin in admin
====================
    go to http://yoursite/admin/skin/add/ and add the skin.

Add skin folders
================
    Add any folders under normal template directories (see `TEMPLATE_DIRS` in settings.py).

    * templates/index.html
    * templates/skin/index.html

    If a view has a ``template_name`` of `'index.html'`, it will first look for it in the `templates/skin` folder, then
    it will look in the `templates` folder (assuming you also have the default Django template loaders set up in
    ``TEMPLATE_LOADERS``.
