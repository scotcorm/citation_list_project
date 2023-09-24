from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=500)
    title2 = models.CharField(max_length=500, blank=True)
    title3 = models.CharField(max_length=500, blank=True)
    creator = models.CharField(max_length=500)
    creator2 = models.CharField(max_length=500, blank=True)
    creator3 = models.CharField(max_length=500, blank=True)
    source = models.URLField()
    source2 = models.URLField(blank=True)
    source3 = models.URLField(blank=True)
    license = models.CharField(max_length=500)
    license2 = models.CharField(max_length=500, blank=True)
    license3 = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='attributions/images/')
    image2 = models.ImageField(upload_to='attributions/images/', blank=True)
    image3 = models.ImageField(upload_to='attributions/images/', blank=True)
