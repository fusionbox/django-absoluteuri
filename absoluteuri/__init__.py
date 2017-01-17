import pkg_resources

from django.core import urlresolvers
from django.conf import settings
from django.contrib.sites.models import Site


__version__ = pkg_resources.get_distribution('django-absoluteuri').version


def build_absolute_uri(path):
    """Turn a relative URL into an absolute URL."""
    return build_absolute_uri_on_site(get_current_site(), path)


def reverse(*args, **kwargs):
    """Reverse a URL and make it absolute."""
    return reverse_on_site(get_current_site(), *args, **kwargs)


def build_absolute_uri_on_site(site, path):
    """Turn a relative URL into an absolute URL on a certain site."""
    return '{protocol}://{domain}{path}'.format(
        protocol=getattr(settings, 'ABSOLUTEURI_PROTOCOL', 'http'),
        domain=site.domain,
        path=path
    )


def reverse_on_site(site, *args, **kwargs):
    """Reverse a URL and make it absolute on a certain site."""
    path = urlresolvers.reverse(*args, **kwargs)
    return build_absolute_uri_on_site(site, path)


def get_current_site():
    return Site.objects.get_current()


def get_site(site_pk):
    return Site.objects.get(pk=site_pk)
