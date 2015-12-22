from django.contrib import admin
from .models import Post
from .forms import PostForm


class TinyMCEAdmin(admin.ModelAdmin):
    form = PostForm
    js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Post, TinyMCEAdmin)
