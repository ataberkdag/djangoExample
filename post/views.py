from django.shortcuts import render
from .models import Post

def postHomePage(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html', {'posts': posts})
# Create your views here.
