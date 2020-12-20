from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    link = models.CharField(max_length=100, blank=False, default='')
    votes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150, blank=False, default='')

    class Meta:
        ordering = ('created',)
