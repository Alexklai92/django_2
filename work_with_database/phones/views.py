from django.shortcuts import render

from .models import Phone

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    if 'sort' in request.GET:
        if request.GET['sort'] == 'name':
            phones = Phone.objects.all().order_by('name')
        elif request.GET['sort'] == 'max_price':
            phones = Phone.objects.all().order_by('-price')
        else:
            phones = Phone.objects.all().order_by('price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_slug = Phone.objects.all().filter(slug=slug)
    context = {'phone_slug': phone_slug}
    return render(request, template, context)
