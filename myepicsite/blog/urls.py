from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.title, name='title'),
    url(r'^title$', views.title, name='title'),
    url(r'^creative$', views.creative, name='creative'),
    url(r'^reviews$', views.reviews, name='reviews'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),

]
