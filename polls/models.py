from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django_extensions.db.models import AutoSlugField

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Contact(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=256)
    contact_user_obj = models.ManyToManyField(User)
    slug = AutoSlugField(populate_from=['first_name', 'last_name'])

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_queryset(self):
        return User.objects.get(id=self.id)
