from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)
    user = models.CharField(max_length=200, default="anon")

