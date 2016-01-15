from django.contrib import admin
from .models import Post, Picture, Review
from .forms import PostForm, PictureForm, ReviewForm
import urllib.request, json


class MyReview(admin.ModelAdmin):

	form = ReviewForm
	exclude = ('author',)
	prepopulated_fields = {"slug": ("title",)}

	def save_model(self, request, obj, form, change):
		if not change:
			# Сохранение авторизованного пользователя как автора поста
			obj.author = request.user
		if obj.position.longitude:
			# Запрос к геокодеру для получения адреса по координатам
			geocode_request = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode=" + str(obj.position.longitude) + "," + str(obj.position.latitude)
			geocode_response = urllib.request.urlopen(geocode_request)
			str_geocode_response = geocode_response.readall().decode('utf-8')
			geocode = json.loads(str_geocode_response)
			# Сохранение адреса
			obj.address = geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
		obj.save()


class MyPost(admin.ModelAdmin):

	form = PostForm
	exclude = ('author',)
	prepopulated_fields = {"slug": ("title",)}

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
