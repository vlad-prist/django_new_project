from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE) # 2 Вариант
    # avatar = models.ImageField(upload_to='students/', verbose_name='аватар', null=True, blank=True) # 1 Вариант
    # null=True значит что мы можем хранить в базе null объекты (пустыне)
    # blank=True значит что мы можем хранить в базе пустые строки

    is_active = models.BooleanField(default=True, verbose_name='Учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('last_name',)
        # Информация для вывода удобного отображения текстов нашей модели
