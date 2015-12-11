from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Picture
from .forms import PostForm, PictureForm
from myepicsite.settings import MEDIA_ROOT
from django.forms.models import inlineformset_factory


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
        

def post_new(request):

    PictureFormset = inlineformset_factory(Post, Picture, form=PictureForm, extra=2)

    if request.method == "POST":

        post_form = PostForm(request.POST)
        picture_formset = PictureFormset(request.POST, request.FILES)

        if post_form.is_valid() and picture_formset.is_valid():

            # Сохранение поста
            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            #Сохранение картинок
            for picture_form in picture_formset:

                picture = picture_form.save(commit=False)
                picture.post = Post.objects.get(pk=post.pk)           
                picture.save()

            # Редирект на страницу с новым постом
            return redirect('blog.views.post_detail', pk=post.pk)

    # Отобразить пустую форму
    else:
        post_form = PostForm()
        picture_formset = PictureFormset()

    # Отобразить страницу с формой
    return render(request, 'blog/post_edit.html', {'post_form': post_form, 'picture_formset': picture_formset})

def post_edit(request, pk):

    # import ipdb; ipdb.set_trace()
    
    PictureFormset = inlineformset_factory(Post, Picture, form=PictureForm, extra=2)
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        post_form = PostForm(request.POST, instance=post)
        picture_formset = PictureFormset(request.POST, instance=post)

        if post_form.is_valid() and picture_formset.is_valid():

            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            for picture_form in picture_formset:

                picture = picture_form.save(commit=False)
                picture.post = Post.objects.get(pk=post.pk)           
                picture.save()

            return redirect('blog.views.post_detail', pk=post.pk)

    else:

        post_form = PostForm(instance=post)
        picture_formset = PictureFormset(instance=post)

    return render(request, 'blog/post_edit.html', {'post_form': post_form, 'picture_formset': picture_formset})