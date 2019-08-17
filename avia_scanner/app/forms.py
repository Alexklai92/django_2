from django import forms

from .widgets import AjaxInputWidget
from .models import City

from datetime import datetime, timedelta

class SearchTicket(forms.Form):
    from_city = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax'), label='Город отправления')
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город прибытия')
    residence_time = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.today() + timedelta(days=14))
