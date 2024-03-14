from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Shop(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cars(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
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

    def get_absolute_url(self):
        return reverse('car:cars', args=(self.id,))

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        return super().save(*args, **kwargs)