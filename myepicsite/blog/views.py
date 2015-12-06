from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm, PictureForm
from myepicsite.settings import MEDIA_ROOT


def creative(request):  
	return render(request, 'blog/creative.html')

def gallery(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')    
    return render(request, 'blog/gallery.html', {'posts' : posts})

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

def handle_uploaded_file(f):
    with open('MEDIA_ROOT', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        

def post_new(request):

    if request.method == "POST":

        post_form = PostForm(request.POST)
        picture_form = PictureForm(request.POST, request.FILES)

        if post_form.is_valid() and picture_form.is_valid():

            #import ipdb; ipdb.set_trace()

            handle_uploaded_file(request.FILES['picture'])

            # Сохранение поста
            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            #import ipdb; ipdb.set_trace()

            #Сохранение картинок
            picture = picture_form.save(commit=False)
            picture.post = Post.objects.get(pk=post.pk)
           
            picture.save()

            # Редирект на страницу с новым постом
            return redirect('blog.views.post_detail', pk=post.pk)

    # Отобразить пустую форму
    else:
        post_form = PostForm()
        picture_form = PictureForm()

    # Отобразить страницу с формой
    return render(request, 'blog/post_new.html', {'post_form': post_form, 'picture_form': picture_form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post_form = PostForm(request.POST)
        picture_form = PictureForm(request.POST)
        if post_form.is_valid() and picture_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            picture = picture_form.save()
            picture.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        icture_form = PictureForm()
    return render(request, 'blog/post_edit.html', {'post_form': post_form, 'picture_form': picture_form})