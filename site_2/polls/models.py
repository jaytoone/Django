from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    was_published_recently.boolean = True
    was_published_recently.admin_order_field = pub_date
    was_published_recently.short_description = 'Publised_recently'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)# 설문조사주제의id 값
    choice_text = models.CharField(max_length=200) # 설문조사주제에대한선택지텍스트
    votes = models.IntegerField(default=0) # 해당선택지의

    def __str__(self):
        return self.choice_text
