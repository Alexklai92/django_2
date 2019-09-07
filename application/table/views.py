import csv

from django.shortcuts import render
from django.views import View
from .models import FilePath, Table

CSV_FILENAME = str(FilePath.objects.get(pk=1))

COLUMNS = Table.objects.all()


class TableView(View):

    def get(self, request):
        with open(CSV_FILENAME, 'rt') as csv_file:
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
            csv_name = CSV_FILENAME.split('\\')[-1]
            result = render(request, 'table.html', {'columns': COLUMNS, 'table': table, 'csv_file': csv_name})
        return result
