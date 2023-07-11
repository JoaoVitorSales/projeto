from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cars(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    uptdate_date = models.DateField(auto_now=True)
    value = models.IntegerField
    value_unit = models.CharField(max_length=8)
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    shop = models.ForeignKey(
        Shop, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
