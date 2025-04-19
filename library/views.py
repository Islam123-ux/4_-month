from django.shortcuts import render
from django.http import HttpResponse

def http_response(request):
    return HttpResponse("Hello, world by Http!")

def render_response(request):
    return render(request, 'library/index.html')    