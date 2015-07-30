from __future__ import absolute_import
import warnings

from django import template

import absoluteuri

register = template.Library()


@register.simple_tag(name='absoluteuri')
def do_absoluteuri(view_name, *args, **kwargs):
    """Reverse a URL and make it absolute."""
    return absoluteuri.reverse(view_name, args=args, kwargs=kwargs)


register.filter(name='absolutize')(absoluteuri.build_absolute_uri)


@register.simple_tag(name='absolutize')
def absolutize_deprecated_tag(*args, **kwargs):
    warnings.warn(
        "{% absolutize %} tag is deprecated. Use {{ |absolutize }} filter",
        DeprecationWarning,
    )
    return absoluteuri.build_absolute_uri(*args, **kwargs)
