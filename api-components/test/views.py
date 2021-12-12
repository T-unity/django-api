from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.views import APIView
from .models import Human

# Create your views here.
class HumanList(ListView):
  template_name = 'human-list.html'
  # HumanListのViewの中で、どのDBテーブルを使用するのか指示する
  model = Human

# シンプルに実装できるため、確認目的でAPIviewを使用（実際はAPIViewはほぼ使わない）
class HumanListAPI(APIView):
  permission_classes = []
