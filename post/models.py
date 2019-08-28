from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name = 'Title')
    summary = models.TextField(verbose_name = 'Summary')
    content = models.TextField(verbose_name = 'Content')
    publishDate = models.DateTimeField(verbose_name = 'Publish Date', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})