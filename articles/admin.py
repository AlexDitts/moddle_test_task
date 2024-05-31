from django.contrib import admin

from articles.models import activities, articles, dicts


class CommentInline(admin.TabularInline):
    model = activities.Comment
    extra = 0


class RatingInline(admin.TabularInline):
    model = activities.Rating
    extra = 0


@admin.register(articles.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    inlines = (
        RatingInline,
        CommentInline,
    )


admin.site.register(articles.Author, admin.ModelAdmin)
admin.site.register(articles.AuthorInfo, admin.ModelAdmin)
admin.site.register(activities.Rating, admin.ModelAdmin)
admin.site.register(activities.Comment, admin.ModelAdmin)
admin.site.register(dicts.Source, admin.ModelAdmin)
admin.site.register(dicts.Tag, admin.ModelAdmin)
