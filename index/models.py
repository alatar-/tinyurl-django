from django.db import models

from .settings import SHORT_URL_LENGTH_BOUNDS


class Url(models.Model):
    destination_url = models.URLField('destination url')
    tiny_url = models.CharField('tiny url', unique=True, max_length=max(10, SHORT_URL_LENGTH_BOUNDS[1]))
    pub_date = models.DateTimeField('date published')
    visit_counter = models.IntegerField('visit counter', default=0)

    def __str__(self):
        return self.tiny_url
