from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
  name = models.TextField(default='')
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name

class Item(models.Model):
  content = models.TextField(default='')
  list_parent = models.ForeignKey(List, on_delete=models.CASCADE)

  def __str__(self):
    return self.content