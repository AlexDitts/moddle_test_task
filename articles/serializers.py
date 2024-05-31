from rest_framework import serializers

from articles.models.articles import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListStatsSerializer(serializers.ModelSerializer):
    # todo: раскомментировать
    count_comments = serializers.IntegerField()
    count_ratings = serializers.IntegerField()
    average_rating = serializers.IntegerField()
    count_comments_mobile = serializers.IntegerField()
    author_age = serializers.IntegerField()
    author_age_in_publish = serializers.IntegerField()
    count_activities = serializers.IntegerField()

    class Meta:
        model = Article
        fields = '__all__'
