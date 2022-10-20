from django import template
import re

register = template.Library()

dictionary = ['Сколково', 'Госуслуг', 'Чубайс', 'Собянин']

@register.filter()
def censor(value):
    new_value = value
    for word in dictionary:
        new_value = new_value.replace(word, word[0]+'...')
    return (new_value)
