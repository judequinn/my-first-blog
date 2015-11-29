from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^creative$', views.creative, name='creative'),
    url(r'^reviews$', views.reviews, name='reviews'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^index$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),

]
