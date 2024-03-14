from django import template

register = template.Library()


@register.filter()
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value

# in template usage:
# {% load filters %}

# {{ form.username|placeholder: 'Email' }}
