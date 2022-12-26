from django.contrib import admin
from .models import Articles, ArticleSeries



class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "slug",
         'author',
        "published",
        'image'
    ]

class ArticleAdmin(admin.ModelAdmin):
       fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'article_slug', 'series', 'author', 'image']}),
        ("Content", {"fields": ['content', 'notes']}),
        ("Date", {"fields": ['modified']})
    ]

# Register your models here.
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Articles,ArticleAdmin)