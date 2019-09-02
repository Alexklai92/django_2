from django.core.management.base import BaseCommand
from map.models import Station, Route

import csv

class Command(BaseCommand):
    help = 'Import data'


    def handle(self, *args, **kwargs):
        with open('moscow_bus_stations.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                station = Station(latitude=float(row[3]), longitude=float(row[2]), name=str(row[1]))
                station.save()

                routes = [route for route in row[7].split('; ')]
                for route in routes:
                    object = Route.objects.filter(name=route).first()
                    if object:
                        station.routes.add(object)
                    else:
                        route = Route(name=route)
                        route.save()
                        station.routes.add(route)
                station.save()
