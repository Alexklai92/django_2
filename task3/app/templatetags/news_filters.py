from django import template

import datetime
import re

register = template.Library()

@register.filter
def format_date(value):
    dt = datetime.datetime.fromtimestamp(int(value))
    now = datetime.datetime.now()

    if (now - dt) < datetime.timedelta(hours=0, minutes=10, seconds=0):
        output = 'Только что'
    elif (now - dt) < datetime.timedelta(hours=24, minutes=0, seconds=0):
        output = f'{(now - dt).seconds // 3600} часов назад'
    else:
        output = dt.strftime('%Y %B %d')
    return output


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if value < -5:
        output = 'всё плохо'
    elif value -5 < value and value < 5:
        output = 'нейтрально'
    else:
        output = 'хорошо'

    print(f'VALUE is "{value}" result is')

    return output

@register.filter
def format_num_comments(value):
    if value <= 0: #кто знает, вдруг там будет когда-нибудь отрицательное значение
        output = 'оставьте комментарий'
    elif value < 50:
        output = f'{value}'
    else:
        output = f'50+'
    return output

@register.filter
def format_selftext(value, count):
    value = value.split(' ')
    start = ' '.join(value[:count])
    end = ' '.join(value[-count:])
    return f'{start} ... {end}'
