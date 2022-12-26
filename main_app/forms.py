from django import forms
from .models import Articles, ArticleSeries
class SeriesCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "slug",
            "image",
        ]

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Articles

        fields = [
            "title",
            "subtitle",
            "article_slug",
            "content",
            "notes",
            "series",
            "image",
        ]

class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "image",
        ]

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Articles

        fields = [
            "title",
            "subtitle",
            "content",
            "notes",
            "series",
            "image",
        ]