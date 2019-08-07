from django.shortcuts import render
from django.views.generic import ListView
from .models import Phone



def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(
        request,
        template,
        context
    )
