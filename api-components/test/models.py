from django.db import models

class Human(models.Model):
  # charfieldは引数にmax_lengthの設定必須
  name = models.CharField(max_length=20)
  greeting = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    # selfなのでオブジェクト自身が持つ情報の何かをreturnできる
    return self.name
    # return self.greeting

class Tweet(models.Model):
  name = models.ForeignKey(Human, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = verbose_name_plural = '投稿一覧'
