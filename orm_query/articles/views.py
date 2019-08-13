from django.views.generic import ListView
#from django.shortcuts import render

from .models import Article, Author

class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all().select_related('author').only('author__name', 'genre', 'title', 'text',)
        context['articles'] = articles
        return context

# def articles_list(request):
#     template_name = 'articles/news.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#
#     return render(request, template_name, context)
