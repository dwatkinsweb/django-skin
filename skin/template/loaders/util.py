from skin.models import SiteSkin


def get_site_skin(site, name):
    """ Return the skin for the requested site
    :param site: Site you are requesting skin for
    :type site: django.contrib.sites.models.Site
    :param name: Name of skin you are requesting
    :type name: str
    :return: Requested skin based on site and name
    :rtype: skin.models.SiteSkin | None
    """
    try:
        return SiteSkin.objects.get(site=site, name=name)
    except SiteSkin.DoesNotExist:
        return None