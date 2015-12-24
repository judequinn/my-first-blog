from django.contrib import admin
from .models import Post, Picture
from .forms import PostForm, PictureForm


class WysiwygAdmin(admin.ModelAdmin):

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

admin.site.register(Post, WysiwygAdmin)
admin.site.register(Picture, MyPicture)
