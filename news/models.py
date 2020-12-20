from django.db import models


# Create your models here.
class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150, blank=False, default='')
    content = models.CharField(max_length=250, blank=True, default='')
