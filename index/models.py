from django.db import models


class Url(models.Model):
    destination_url = models.URLField('destination url')
    tiny_url = models.CharField('tiny url', max_length=10)
    pub_date = models.DateTimeField('date published')
    visit_counter = models.IntegerField('visit counter', default=0)
