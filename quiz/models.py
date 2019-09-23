from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
  name = models.TextField(default='')
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Question(models.Model):
  quiz_parent = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
  question = models.TextField(null=False)
  correct_answer = models.TextField(null=False)
  answers= ArrayField(models.TextField(null=False), default=[])
