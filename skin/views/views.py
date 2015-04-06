from django.contrib.sites.models import Site
from django.utils._os import safe_join
from django.views.generic import TemplateView

from skin.conf import settings
from skin.template.loaders.util import get_site_skin


class TemplateSkinView(TemplateView):
    """
    A view that extends Djangos base TemplateView to allow you to set up skins.
    """
    skin_name = None
    skin_path = None

    def get_skin_name(self):
        if self.skin_name is None:
            return settings.SKIN_NAME
        else:
            return self.skin_name

    def get_skin(self):
        return get_site_skin(site=Site.objects.get_current(), name=self.get_skin_name())

    def get_skin_path(self):
        if self.skin_path is not None:
            return self.skin_path

        skin = self.get_skin()
        if skin is not None:
            return skin.path
        else:
            return None

    def get_template_names(self):
        template_names = super(TemplateSkinView, self).get_template_names()
        skin_path = self.get_skin_path()
        skin_template_names = []
        if skin_path is not None:
            for template_name in template_names:
                skin_template_names.append(safe_join(skin_path, template_name))
        return skin_template_names + template_names