from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scopeship


class ArticleView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Article.objects.all()
        context['data'] = object_list
        context['tags'] = {}
        for item in object_list:
            context['tags'][item.id] = {}
            tags = Scopeship.objects.all().filter(article=item.id).order_by('-is_main', 'scope__topic')
            context['tags'][item.id] = tags
        return context
