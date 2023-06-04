from django.db import models
from django.contrib.auth.models import AbstractUser


class GutenbergText(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    page = models.IntegerField()

    class Meta:
        using = 'gutenberg'


class User(AbstractUser):
    library = models.ManyToManyField(GutenbergText, related_name='users')

    class Meta:
        using = 'default'
