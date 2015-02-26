import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    blog_content = models.TextField()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title_text
