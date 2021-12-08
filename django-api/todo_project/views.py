from django.http import HttpResponse

def helloworldfunction(req):
  resobj = HttpResponse('hello world')
  return resobj
