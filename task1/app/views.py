from django.shortcuts import render

import csv
import os
from django.conf import settings

def inflation_view(request):
    template_name = 'inflation.html'

    csv_path = os.path.join(settings.BASE_DIR, 'inflation_russia.csv')

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        values = list()
        for row in reader:
            key = ''.join(row)
            values.append(row[key].split(';'))

        table_heads = key.split(';')

    context = {
        'table_heads': table_heads,
        'values': values
    }

    return render(request, template_name,
                  context)
