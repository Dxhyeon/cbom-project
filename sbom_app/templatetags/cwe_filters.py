from django import template

register = template.Library()

@register.filter(name='extract_cwe_number')
def extract_cwe_number(value):
    if value.startswith('CWE-'):
        return value[4:] 
    return value

@register.filter(name='is_number')
def is_number(value):
    return value.isdigit()