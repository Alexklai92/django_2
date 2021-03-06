from datetime import datetime as dt
from django.conf import settings
import os
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from dateutil.parser import parse



class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None, **kwargs):
        context = super().get_context_data(**kwargs)
        file_list = []
        if date is not None:
            try:
                get_date_obj = parse(date).strftime("%Y-%m-%d")
            except:
                get_date_obj = ''

        for file in os.listdir(settings.FILES_PATH):
            file_stats = os.stat(os.path.join(settings.FILES_PATH, file))
            file_info = {
                'name': file,
                'ctime': dt.fromtimestamp(file_stats.st_ctime),
                'mtime': dt.fromtimestamp(file_stats.st_mtime),
            }

            if date is None or get_date_obj == dt.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d") \
                or get_date_obj == dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"):
                file_list.append(file_info)

        context.update({
            'files': file_list,
            'date': date
        })
        return context


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    if not os.path.isfile(os.path.join(settings.FILES_PATH, name)):
        error = 'Файл {} не существует'.format(name)
        context ={'file_name': name, 'file_content': None, 'error': error}

    else:
        with open(os.path.join(settings.FILES_PATH, name), encoding='utf8') as necessary_file:
            file_content = necessary_file.read()
            context ={'file_name': name, 'file_content': file_content}
    return render(
               request,
               'file_content.html',
               context
           )
