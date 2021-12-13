from django.urls import path
from .views import HumanList, HumanListAPI, TweetView

urlpatterns = [
    # django's view
    path('list', HumanList.as_view()),
    path('tweet-list/', TweetView.as_view()),
    # rest_framework's view
    path('api/human/', HumanListAPI.as_view()),
]
