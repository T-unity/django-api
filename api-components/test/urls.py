from django.urls import path
from .views import HumanList, HumanListAPI

urlpatterns = [
    # django's view
    path('list', HumanList.as_view()),
    # rest_framework's view
    path('api/', HumanListAPI.as_view()),
]
