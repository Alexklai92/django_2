from django.db import models

class Scope(models.Model):
    topic = models.CharField(max_length=25, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Scope, through='Scopeship')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class Scopeship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopeship')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    is_main = models.BooleanField(u'Главная')

    # class Meta:
    #     verbose_name = 'Тематика статьи'
    #     verbose_name_plural = 'Тематика статьи'

    def __str__(self):
        return f'{self.article}_{self.scope}'
