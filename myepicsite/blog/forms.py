from django import forms
from .models import Post
from myepicsite.widgets import AdvancedEditor


class PostForm(forms.ModelForm):

    text = forms.CharField(widget=AdvancedEditor())

    class Meta:

        model = Post
        fields =  ['author', 'title', 'tag', 'created_date', 'published_date']
        labels = {
                'author': ('Автор:'),
                'title': ('Заголовок поста:'),
                'tag': ('Раздел:'),
                'created_date': ('Дата создания:'),
                'published_date': ('Дата публикации:'),
        }
