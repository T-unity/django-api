from django.urls import path
from .views import HumanList, HumanListAPI, TweetView, TweetAPIView, TweetListAPI

urlpatterns = [
    # rest_framework's view
    path('api/human/', HumanListAPI.as_view()),
    path('api/tweet/', TweetListAPI.as_view()),
    path('api/tweet/<int:pk>/', TweetAPIView.as_view()),
]
