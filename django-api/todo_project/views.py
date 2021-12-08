from django.http import HttpResponse
# 汎用ビュー
from django.views.generic import TemplateView

# function based view
def helloworldfunction(req):
  resobj = HttpResponse('hello world')
  return resobj

# class based view
# インポートした汎用ビューを使用
class HelloWorldClass(TemplateView):
  template_name = 'hello.html'
