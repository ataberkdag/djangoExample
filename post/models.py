from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name = 'Title')
    summary = models.TextField(verbose_name = 'Summary')
    content = models.TextField(verbose_name = 'Content')
    publishDate = models.DateTimeField(verbose_name = 'Publish Date')

    def __str__(self):
        return self.title
