# Generated by Django 3.2.7 on 2021-09-26 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.worker')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('long', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата посещения')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
            options={
                'verbose_name': 'Посещение',
                'verbose_name_plural': 'Посещения',
            },
        ),
    ]
