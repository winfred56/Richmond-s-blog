from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

posts = Post.objects.all().exclude(id=-1).order_by('-date_posted')
#first_post = Post.objects.get(id=1)
nth_post = Post.objects.latest('date_posted')
context = {
    'posts':posts,
    #'first_post':first_post,
    'nth_post':nth_post
}
def HomeView(request):

    return render(request, 'post/responsive.html', context)


def AboutView(request):
    
    return render(request,'post/about-me.html', context)


def RecentView(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts':posts
    }
    return render(request,'post/recent-posts.html', context)

