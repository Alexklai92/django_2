from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Route, Station

# Create your views here.
def get_list(request):
    context = {}
    route = request.GET.get('route', None)
    if route:
        stations = Station.objects.filter(routes__name=route)
        context['stations'] = stations

        stations = stations.order_by('longitude')
        st_first = stations.first()
        st_last = stations.last()
        x = (st_first.longitude + st_last.longitude) / 2

        stations = stations.order_by('latitude')
        st_first = stations.first()
        st_last = stations.last()
        y = (st_first.latitude + st_last.latitude ) / 2

        context['center'] = {'x': x, 'y': y}

    context['routes'] = Route.objects.all()

    return render(request, 'stations.html', context)
