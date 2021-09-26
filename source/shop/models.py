from django.db import models

from worker.models import Worker


class Shop(models.Model):
    name = models.CharField('Название', max_length=128)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.name


class Visit(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    lat = models.DecimalField('Широта', max_digits=9, decimal_places=6)
    long = models.DecimalField('Долгота', max_digits=9, decimal_places=6)
    date = models.DateTimeField('Дата посещения', auto_now_add=True)

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return f'{self.shop} - {self.date:%Y-%m-%d %H:%M:%S}'
