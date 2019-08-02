from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()

def index(request):
    from_landing = request.GET.get('from-landing', None)
    counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg', None)
    if ab_test_arg == 'test':
        counter_show[ab_test_arg] += 1
        return render_to_response('landing_alternate.html')
    counter_show[ab_test_arg] += 1
    return render_to_response('landing.html')


def stats(request):
    result_test = counter_click['test'] / counter_show['test'] if counter_show['test'] != 0 else 0
    result_original = counter_click['original'] / counter_show['original'] if counter_show['original'] != 0 else 0
    return render_to_response('stats.html', context={
        'test_conversion': round(result_test, 1),
        'original_conversion': round(result_original, 1),
    })
