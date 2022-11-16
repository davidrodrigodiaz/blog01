from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    #este es un comentario
    posts = Post.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
    #posts=Post.objects.all

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(pk, request):
    post = get_object_or_404(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
