from django import template


register = template.Library()


@register.filter
def format_percent(value):
    """
    0.2543 => 25.4
    """
    return '{0:.1f}'.format(float(value) * 100)
