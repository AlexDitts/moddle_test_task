from django.db import models


class Comment(models.Model):
    article = models.ForeignKey(
        'Article', models.CASCADE, 'comments',
        verbose_name='Статья'
    )
    message = models.TextField('Сообщение')
    source = models.ForeignKey(
        'Source', models.RESTRICT, 'comments',
        verbose_name='Источник', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Комментарий к статьям'
        verbose_name_plural = 'Комментарии к статьям'

    def __str__(self):
        return f'Комментарий {self.pk}'


class Rating(models.Model):
    article = models.ForeignKey(
        'Article', models.CASCADE, 'ratings',
        verbose_name='Статья'
    )
    rate = models.PositiveSmallIntegerField('Оценка')
    source = models.ForeignKey(
        'Source', models.RESTRICT, 'ratings',
        verbose_name='Источник', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Оценка к статьям'
        verbose_name_plural = 'Оценки к статьям'

    def __str__(self):
        return f'Оценка {self.pk}'
