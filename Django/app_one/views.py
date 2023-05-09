from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = "<html><body><h1>Welcome to my Home Page</h1></body></html>"
    return HttpResponse(content)

def demo(request):
    path = request.path
    method = request.method
    content = f"<html><body><h1>Welcome to my Demo Page</h1><p>Path: {path}</p><p>Method: {method}</p></body></html>"
    return HttpResponse(content)
