from django.urls import path

from articles import views

urlpatterns = [
    path('stats/', views.ArticleListStatsView.as_view()),
    path('', views.ArticleListView.as_view()),
]
