from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
