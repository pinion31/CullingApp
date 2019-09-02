from django.db import models

# Create your models here.
class List(models.Model):
  name = models.TextField(default='')

  def __str__(self):
    return self.name

class Item(models.Model):
  content = models.TextField(default='')
  list_parent = models.ForeignKey(List, on_delete=models.CASCADE)

  def __str__(self):
    return self.content