from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    body = models.TextField(verbose_name='Содержимое')

    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
