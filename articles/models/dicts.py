from django.db import models


class Source(models.Model):
    code = models.CharField('Код', max_length=31, primary_key=True, unique=True)
    name = models.CharField('Название', max_length=64)

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'

    def __str__(self):
        return f'Источник {self.pk}'


class Tag(models.Model):
    code = models.CharField('Код', max_length=31, primary_key=True, unique=True)
    name = models.CharField('Название', max_length=64)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'Тег {self.pk}'