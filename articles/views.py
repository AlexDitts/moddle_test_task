import datetime

from django.db.models import Count, Q, F, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from articles.filters import ArticleFilter
from articles.models.articles import Article
from articles import serializers


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilter


class Average:
    pass


class ArticleListStatsView(ListAPIView):
    # queryset = Article.objects.all()
    serializer_class = serializers.ArticleListStatsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ArticleFilter

    def get_queryset(self):
        return Article.objects.annotate(
            count_comments=Count('comments'),
            count_ratings=Count('ratings'),
            average_rating=Avg('ratings__rate'),
            count_comments_mobile=Count('comments', filter=Q(comments__source__code='mobile')),
            author_age=datetime.datetime.now().year - F('author__dob__year'),
            author_age_in_publish=(F('publish_date__year') - F('author__dob__year')),
            count_activities=Count('comments') + Count('ratings'),
        )
