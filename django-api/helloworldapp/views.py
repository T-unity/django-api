from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworldappview(req):
  return HttpResponse('<h1>this page made by helloworldapp and function based view</h1>')
