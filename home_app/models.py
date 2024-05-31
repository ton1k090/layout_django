from django.db import models


class Trainer(models.Model):
    name = models.CharField('Имя тренера', max_length=50)
    image = models.ImageField('Фото',upload_to='media/trainers/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'



