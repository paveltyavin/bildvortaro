# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def dotted_number(number):
    number = float(number)
    return format(number, '.', 6)
