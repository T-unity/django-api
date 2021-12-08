from django.contrib import admin
from django.urls import path, include
# 同階層のviewsからhelloworldfunctionをimport
from .views import helloworldfunction, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    # プロジェクト内のviews.pyにあるhelloworldfunctionをcall
    path('helloworld/', helloworldfunction),
    # class based viewでcallするhtmlファイル
    # クラスビューの場合は、views.pyで作成したクラスに.as_viewをつける必要がある
    path('helloworld2/', HelloWorldClass.as_view())
]
