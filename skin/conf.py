from django.conf import settings

settings.SKIN_NAME = getattr(settings, 'SKIN_NAME', None)