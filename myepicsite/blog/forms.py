from django import forms
from .models import Post, Picture


class AdvancedEditor(forms.Textarea):

    class Media:

        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',]


class PostForm(forms.ModelForm):

    text = forms.CharField(widget=AdvancedEditor(), label='Содержание')

    class Meta:

        model = Post
        fields =  ['author', 'title', 'tag', 'created_date', 
        		   'published_date', 'c_latitude', 'c_longitude']


class PictureForm(forms.ModelForm):

    class Meta:

        model = Picture
        fields =  ['author', 'title', 'created_date', 
                   'published_date', 'picture', 'comment']

