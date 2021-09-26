from django.db import models


class Worker(models.Model):
    name = models.CharField('Имя', max_length=128)
    phone = models.CharField('Телефон', max_length=32)

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'

    def __str__(self):
        return self.name
