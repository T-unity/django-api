# https://docs.djangoproject.com/ja/3.2/ref/request-response/#django.http.HttpResponse
from django.http import HttpResponse

# viewsの関数はリクエストオブジェクトを受け取って
# レスポンスオブジェクトをreturnする
# 引数でリクエストオブジェクトを取得（名前は何でもOK）
def helloworldfunction(req):
  # まずDjangoコアのHttpResponseクラスを返す
  return HttpResponse('')
