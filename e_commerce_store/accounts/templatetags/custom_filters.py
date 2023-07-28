from django import template

register = template.Library()


@register.filter
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value


@register.filter
def disable_field(value):
    value.field.widget.attrs['readonly'] = True
    return value
