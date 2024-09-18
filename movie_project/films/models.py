from django.db import models


class Movie(models.Model):
    name = models.CharField('Название фильма', max_length=100)
    describe = models.TextField('Описание фильма')
    comment = models.TextField('Отзыв')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name

