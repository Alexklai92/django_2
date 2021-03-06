from django.shortcuts import render
from django.views import View

from .forms import CalcForm

def calc_view(request):
    template = "app/calc.html"
    if request.method == "GET":
        form = CalcForm(request.GET or None)
        if form.is_valid():
            initial_fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months_count = form.cleaned_data['months_count']
            common_result = initial_fee + initial_fee * rate/100
            result =  (initial_fee + initial_fee * rate/100) / months_count
            context = {
                'form': form,
                'common_result': round(common_result, 2),
                'result': round(result, 2)
            }
            return render(request, template, context)
        return render(request, template, {'form':form})
    else:
        form = CalcForm()
        return render(request, template, {'form':form})


class CalcView(View):
    template_name = "app/calc.html"
    form_class = CalcForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.is_valid():
            initial_fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months_count = form.cleaned_data['months_count']
            common_result = initial_fee + initial_fee * rate/100
            result =  (initial_fee + initial_fee * rate/100) / months_count
            return render(request, self.template_name, {'form':form,
                         'common_result':common_result, 'result':result})
        return render(request, self.template_name, {'form':form})
