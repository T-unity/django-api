from django.urls import path
from .views import HumanList

urlpatterns = [
    path('list', HumanList.as_view())
]
