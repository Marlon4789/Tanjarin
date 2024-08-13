from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(null=True, max_length=200, blank=False, unique=True)
    description = models.CharField(null=True, max_length=200, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField()
    date = models.DateField(default=timezone.now)
