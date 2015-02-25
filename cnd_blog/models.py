import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    blog_content = models.TextField()

    def __str__(self):
        return self.title_text
