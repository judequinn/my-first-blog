from django import forms
from .models import Post, Picture
from sorl.thumbnail import ImageField


class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        exclude = ['author', 'created_date', 'published_date']

        labels = {

        		'title': ('Заголовок поста:'),
        		'text': ('Текст:'),
        		'tag': ('Раздел:'),

        }


class PictureForm(forms.ModelForm):

	class Meta:

		model = Picture
		exclude = ['post']

		labels = {

				'picture': ('Прикрепить картинку:'),
				'comment': ('Комментарий:'),

		}