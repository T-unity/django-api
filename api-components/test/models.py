from django.db import models

class Human(models.Model):
  # charfieldは引数にmax_lengthの設定必須
  name = models.CharField(max_length=20)
  greeting = models.CharField(max_length=50)
