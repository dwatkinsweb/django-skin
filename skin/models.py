from __future__ import unicode_literals
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSkin(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('Site'))
    name = models.CharField(verbose_name=_('Skin Name'), max_length=20, null=False, blank=False, db_index=True)
    path = models.CharField(verbose_name=_('Path Prefix'), max_length=255, blank=True, default='',
                            help_text=_('Enter the path to add to any existing paths template loaders will look.\n'
                                        'The path used will be {base_dir}{skin_path}{template_name}.'))

    class Meta:
        unique_together = ('site', 'name')

    def __unicode__(self):
        return '<SiteSkin: {site}.{name} - {path}>'.format(self.site.name, self.name, self.path)