from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name: models.CharField(max_length=50)
# Create your models here.
class cars(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    uptdate_date = models.DateField(auto_now=True)
    value = models.IntegerField
    value_unit = models.CharField(max_length=8)
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )