from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 

def http_response(request):
    return HttpResponse("Hello, world by Http!")

def render_response(request):
    return render(request, 'index.html')   

def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})
    

def post_detail_view(request, id):
    if request.method == "GET":
       post = Post.objects.get(id=id)
       return render(request, 'posts/post_detail.html', {'post': post})