from django import forms
from .models import Post, Picture, Review


class AdvancedEditor(forms.Textarea):

    class Media:

        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',]


class PostForm(forms.ModelForm):

    text = forms.CharField(widget=AdvancedEditor(), label='Содержание')

    class Meta:

        model = Post
        fields =  ['author', 'title', 'tag', 'slug', 
                   'published_date']


class PictureForm(forms.ModelForm):

    class Meta:

        model = Picture
        fields =  ['author', 'title', 
                   'published_date', 'picture', 'comment']


class ReviewForm(forms.ModelForm):

    text = forms.CharField(widget=AdvancedEditor(), label='Содержание')

    class Meta:

        model = Review
        fields =  ['author', 'title', 'tag', 'slug',
                   'published_date', 'address', 'position']
