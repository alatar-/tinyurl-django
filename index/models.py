from random import randint

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .settings import TINY_URL_LENGTH_BOUNDS


class ParentUserManager(UserManager):

    def random(self):
        count = self.count()
        print(count)
        assert count, "Users table is empty!"
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class User(AbstractUser):
    objects = ParentUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Url(models.Model):
    user = models.ForeignKey(User)
    destination_url = models.URLField('destination url', unique=True)
    tiny_url = models.CharField('tiny url', unique=True, max_length=max(10, TINY_URL_LENGTH_BOUNDS[1]))
    pub_date = models.DateTimeField('date published')
    visit_counter = models.IntegerField('visit counter', default=0)

    def __str__(self):
        return self.tiny_url
