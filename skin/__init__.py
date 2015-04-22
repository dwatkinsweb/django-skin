__version__ = '0.1.2'

try:
    # noinspection PyUnresolvedReferences
    from django.conf import settings as django_settings

    if 'skin' in django_settings.INSTALLED_APPS:
        # noinspection PyUnresolvedReferences
        from skin.conf import settings
except ImportError:  # pragma: no cover
    """
    This exception means that either the application is being built, or is
    otherwise installed improperly.
    """
    pass