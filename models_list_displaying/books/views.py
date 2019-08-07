from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs:
            sort_date = self.kwargs['date']
            books = Book.objects.order_by('pub_date')
            prev_obj = books.filter(pub_date__lt=sort_date).last()
            if prev_obj:
                context['prev_date'] = str(prev_obj.pub_date)

            next_obj = books.filter(pub_date__gt=sort_date).first()
            if next_obj:
                context['next_date'] = str(next_obj.pub_date)

        return context

    def get_queryset(self):
        if self.kwargs:
            books = Book.objects.filter(pub_date=self.kwargs['date'])
            return books
        else:
            return Book.objects.all()
