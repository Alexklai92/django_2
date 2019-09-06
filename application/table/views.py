import csv

from django.shortcuts import render
from django.views import View
from .models import TableFieldSettings, Path

csv_filename = 'phones.csv'

pathToCsv = Path().get_path

if pathToCsv == '' or pathToCsv != csv_filename:
    Path().set_path(csv_filename)

else:
    csv_filename = pathToCsv

columns = TableFieldSettings.objects.values()

if len(columns) == 0:
    TableFieldSettings.objects.create(title='id', width=1, index=1)
    TableFieldSettings.objects.create(title='name', width=3, index=2)
    TableFieldSettings.objects.create(title='price', width=2, index=3)
    TableFieldSettings.objects.create(title='release_date', width=2, index=4)
    TableFieldSettings.objects.create(title='lte_exists', width=1, index=5)

    columns = TableFieldSettings.objects.values()


class TableView(View):

    def get(self, request):
        with open(csv_filename, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request, 'table.html', {'columns': columns, 'table': table, 'csv_file': csv_filename})
        return result
