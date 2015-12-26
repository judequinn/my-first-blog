from django.contrib import admin
from .models import Post, Picture
from .forms import PostForm, PictureForm
import urllib.parse, urllib.request, json


class WysiwygAdmin(admin.ModelAdmin):

	form = PostForm
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
			obj.coordinates = geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
			obj.c_latitude = float(geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1])
			obj.c_longitude = float(geocode['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[0])
		obj.save()


class MyPicture(admin.ModelAdmin):

	form = PictureForm
	exclude = ('author',)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
		obj.save()

admin.site.register(Post, WysiwygAdmin)
admin.site.register(Picture, MyPicture)
