# -*- encoding:utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if pattern in request.path:
        return 'active'
    return ''


@register.filter
def row_start(counter, cols):
    return int(counter) % int(cols) == 0


@register.filter
def row_end(counter, cols):
    return int(counter + 1) % int(cols) == 0
