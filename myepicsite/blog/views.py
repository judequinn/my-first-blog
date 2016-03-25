from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Picture, Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def creative(request):

    return render(request, 'blog/creative.html')


def gallery(request):

    pictures = Picture.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')    
    return render(request, 'blog/gallery.html', {'pictures' : pictures})


def reviews(request): 

    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # Список разделов
    sections = Review.SECTION_CHOICES
    # Набор цветов для меток на карте
    colors = ['blue', 'red', 'green', 'yellow', 'darkOrange',
                'night', 'darkBlue', 'pink', 'gray',
                'brown', 'darkGreen', 'violet', 'black',  
                'orange', 'lightBlue', 'olive',
             ]
    # Соотнесение раздела, цвета и тэга
    dots = []
    l = len(colors)
    i = 0
    for section in sections:
        if section[0]:
            if i >= l:
                dots.append((section[1], colors[i-l], section[0]))
            else:
                dots.append((section[1], colors[i], section[0]))
            i += 1
    return render(request, 'blog/reviews.html', {'reviews' : reviews, 'dots' : dots})


def index(request):

    return render(request, 'blog/index.html')


def contact(request):

    return render(request, 'blog/contact.html') 


def accessories(request):

    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_list, 10) # Показать по 10 постов на странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не целое число, показать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если номер страница не существует, показать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/accessories.html', {'posts' : posts})


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def review_detail(request, slug):

    review = get_object_or_404(Review, slug=slug)
    return render(request, 'blog/review_detail.html', {'review': review})
