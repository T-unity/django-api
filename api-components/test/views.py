from django.shortcuts import render
from django.views.generic import ListView
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from .models import Human
from .serializers import HumanSerializer

# Create your views here.
class HumanList(ListView):
  template_name = 'human-list.html'
  # HumanListのViewの中で、どのDBテーブルを使用するのか指示する
  model = Human

# シンプルに実装できるため、確認目的でAPIviewを使用（実際はAPIViewはほぼ使わない）
# class HumanListAPI(APIView):
  # permission_classes = []

class HumanListAPI(ListCreateAPIView):
  # ListCreateAPIViewで使用するモデルを指定
  queryset = Human.objects.all()
  # 扱うデータをシリアライズする
  serializer_class = HumanSerializer
  permission_classes = []
