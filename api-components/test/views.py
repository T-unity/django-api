from django.shortcuts import render
from django.views.generic import ListView
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Human, Tweet
from .serializers import HumanSerializer, TweetSerializer

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

class TweetView(ListView):
  model = Tweet
  template_name = 'tweet.html'

# RetrieveAPIView→個別のデータを取得する時に使用する。DetailViewのような感じなのでリソースのIDをクエリに含める必要あり
class TweetAPIView(RetrieveAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
  permission_classes = [IsAuthenticated]
