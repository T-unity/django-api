from django.shortcuts import render
from django.views.generic import ListView
from .models import Human

# Create your views here.
class HumanList(ListView):
  template_name = 'human-list.html'
  # HumanListのViewの中で、どのDBテーブルを使用するのか指示する
  model = Human
