from django import template

register = template.Library()


@register.filter
def stylize(value, row):
    if value:
        index = row.index(value)
        val = float(value)

        if index == len(row) -1:
            return 'grey'
        elif index != 0 and index != 13:
            if val < 0:
                return 'green'
            elif 2 >= val > 1:
                return '#FCA4B3'
            elif 5 >= val > 2:
                return '#FF0B2B'
            elif val > 4:
                return '#c40b21'
