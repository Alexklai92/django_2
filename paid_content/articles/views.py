from django.shortcuts import render
from .models import Article, User


def show_articles(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    user_paid = False
    user = User.objects.filter(username=request.user)
    for value in user:
        user_paid = value.buy_paidcontent
    article = Article.objects.filter(id=id)
    context = {}
    for art in article:
        if art.is_paid and not user_paid:
            context = {
                'paid': 'Это платный контент. Необходимo подписаться!'
            }
        context['article'] = article
    if request.method == 'POST':
        User.objects.filter(username=request.user).update(buy_paidcontent=True)
    return render(
        request,
        'article.html',
        context
    )
