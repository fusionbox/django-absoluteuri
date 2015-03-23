import pkg_resources

from django.core import urlresolvers
from django.conf import settings

__version__ = pkg_resources.get_distribution('django-absoluteuri').version


def build_absolute_uri(path):
    """Turn a relative URL into an absolute URL."""
    from django.contrib.sites.models import Site
    site = Site.objects.get_current()
    return '{protocol}://{domain}{path}'.format(
        protocol=getattr(settings, 'ABSOLUTEURI_PROTOCOL', 'http'),
        domain=site.domain,
        path=path
    )


def reverse(*args, **kwargs):
    """Reverse a URL and make it absolute."""
    path = urlresolvers.reverse(*args, **kwargs)
    return build_absolute_uri(path)
