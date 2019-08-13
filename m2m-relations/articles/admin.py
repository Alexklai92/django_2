from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopeship, Scope

class ScopeshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                counter_topics += 1

        if counter_topics == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if counter_topics > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeshipInline(admin.TabularInline):
    model = Scopeship
    formset = ScopeshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeshipInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    ordering = ['topic']
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass
