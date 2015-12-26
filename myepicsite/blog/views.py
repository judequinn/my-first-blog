from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Picture, Review


def creative(request):  
	return render(request, 'blog/creative.html')


def gallery(request):
    pictures = Picture.objects.filter(published_date__lte=timezone.now()).order_by('published_date')    
    return render(request, 'blog/gallery.html', {'pictures' : pictures})


def reviews(request): 
    return render(request, 'blog/reviews.html')


def index(request):
    return render(request, 'blog/index.html')


def contact(request):
    return render(request, 'blog/contact.html') 


def accessories(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/accessories.html', {'posts' : posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def shops(request):
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/shops.html', {'reviews' : reviews})