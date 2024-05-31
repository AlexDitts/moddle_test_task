from django.db import models


class Author(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    dob = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.full_name} ({self.pk})'


class AuthorInfo(models.Model):
    author = models.OneToOneField(
        Author, models.CASCADE, related_name='info',
        verbose_name='Автор', primary_key=True, unique=True,
    )
    email = models.EmailField('Email', null=True, blank=True)
    phone = models.CharField('Phone', max_length=31, null=True, blank=True)

    class Meta:
        verbose_name = 'Инфо об авторе'
        verbose_name_plural = 'Инфо об авторе'


class Article(models.Model):
    author = models.ForeignKey(
        Author, models.CASCADE, 'articles',
        verbose_name='Автор',
    )
    title = models.CharField('Название статьи', max_length=255)
    text = models.TextField('Содержание стати')
    publish_date = models.DateField('Дата публикации', null=True, blank=True)
    tags = models.ManyToManyField(
        'Tag', related_name='articles', verbose_name='Теги',
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Статья {self.pk}'
