from __future__ import absolute_import

from django import template

import absoluteuri

register = template.Library()


@register.simple_tag(name='absoluteuri')
def do_absoluteuri(view_name, *args, **kwargs):
    """Reverse a URL and make it absolute."""
    return absoluteuri.reverse(view_name, args=args, kwargs=kwargs)


register.simple_tag(name='absolutize')(absoluteuri.build_absolute_uri)
register.filter(name='absolutize')(absoluteuri.build_absolute_uri)
