from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def postHomePage(request):
    posts = Post.objects.all()
    return render(request, 'post/home.html', {'posts': posts})

def postDetailPage(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)

def postCreatePage(request):

    ## You can use this way
    #if request.method == "POST":
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #else:
    #    form = PostForm()

    ## But with this way will be better
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'form': form}
    return render(request, 'post/form.html', context)