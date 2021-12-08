from django.contrib import admin
from django.urls import path, include
# 同階層のviewsからhelloworldfunctionをimport
from .views import helloworldfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    # プロジェクト内のviews.pyにあるhelloworldfunctionをcall
    path('helloworld/', helloworldfunction),
]
