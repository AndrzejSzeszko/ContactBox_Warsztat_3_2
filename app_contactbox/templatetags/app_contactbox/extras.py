#!/usr/bin/python3.7
from django.template import Library

register = Library()


@register.filter
def filter_all(object_manager):
    return object_manager.all()
