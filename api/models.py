from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name="Наименование товара",
                            max_length=50)
    description = models.TextField(verbose_name="Описание",
                                   max_length=100)
    price = models.PositiveIntegerField(verbose_name="Стоимость")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('name',)

    def __str__(self):
        return self.name[15:]

    def convert_cents_to_dollar(self):
        return "{0:.2f}".format(self.price/100)
