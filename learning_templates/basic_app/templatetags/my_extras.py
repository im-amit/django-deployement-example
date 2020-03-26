from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    TThis cut out all values if 'arg' from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)