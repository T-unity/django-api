from rest_framework import serializers

from .models import Human

class HumanSerializer(serializers.ModelSerializer):
  # Metaクラスを使う事でHumanSerializerクラスがMetaクラスのインスタンスになる
  class Meta:
    model = Human
    fields = ['name', 'greeting'] # fieldsで表示するデータを選択
