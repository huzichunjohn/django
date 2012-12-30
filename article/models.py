from django.db import models

# Create your models here.
class List(models.Model):
  title = models.CharField(max_length=250,unique=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']

import datetime
class Item(models.Model):
  title = models.CharField(max_length=250)
  created_date = models.DateTimeField(default=datetime.datetime.now)
  completed = models.BooleanField(default=False)
  article_list = models.ForeignKey(List)
  
  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['-created_date','title']
