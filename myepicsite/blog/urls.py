from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.title, name='title'),
    url(r'^title$', views.title, name='title'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    '''url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),'''
]
