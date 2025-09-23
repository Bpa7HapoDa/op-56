from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='создайте тег')

    def __str__(self):
        return self.name

class Clothes(models.Model):
    title = models.CharField(max_length=200,  verbose_name='Название товара')
    description = models.TextField(blank=True,  verbose_name='Описание товара')
    tags = models.ManyToManyField(Tag, related_name='clothes',  verbose_name='добавьте теги')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Введите цену')

    def __str__(self):
        return self.title
