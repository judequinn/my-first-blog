from django.contrib import admin
from .models import Post, Picture, Review
from .forms import PostForm, PictureForm, ReviewForm
import urllib.parse, urllib.request, json


class MyReview(admin.ModelAdmin):

	form = ReviewForm
	exclude = ('author',)

	def save_model(self, request, obj, form, change):
		if not change:
			# Сохранение авторизованного пользователя как автора поста
			obj.author = request.user
		if obj.address:
			# Запрос к яндексу для получения координат по адресу
			geocode_request = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode=" + urllib.parse.quote_plus(obj.address)
			geocode_response = urllib.request.urlopen(geocode_request)
			str_geocode_response = geocode_response.readall().decode('utf-8')
			geocode = json.loads(str_geocode_response)
			# Сохранение координат
			obj.c_latitude = geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1]
			obj.c_longitude = geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[0]
		obj.save()


class MyPost(admin.ModelAdmin):

	form = PostForm
	exclude = ('author',)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
		obj.save()


class MyPicture(admin.ModelAdmin):

	form = PictureForm
	exclude = ('author',)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
		obj.save()

admin.site.register(Post, MyPost)
admin.site.register(Picture, MyPicture)
admin.site.register(Review, MyReview)
