from skin.models import SiteSkin


skin_cache = {}


def get_site_skin(site, name):
    """ Return the skin for the requested site
    :param site: Site you are requesting skin for
    :type site: django.contrib.sites.models.Site
    :param name: Name of skin you are requesting
    :type name: str
    :return: Requested skin based on site and name
    :rtype: skin.models.SiteSkin | None
    """
    if site.name not in skin_cache or name not in skin_cache[site.name]:
        if site.name not in skin_cache:
            skin_cache[site.name] = {}
        try:
            skin_cache[site.name][name] = SiteSkin.objects.get(site=site, name=name)
        except SiteSkin.DoesNotExist:
            return None
    return skin_cache[site.name][name]