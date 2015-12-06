from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField


# Посты
class Post(models.Model):

    SECTION_CHOICES = ( (None, 'Выбрать раздел'), ('gallery', 'Галерея'),('reviews', 'Обзоры'), ('accessories', 'Аксессуары') )

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    tag = models.CharField(max_length=30, choices=SECTION_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Картинки
class Picture(models.Model):

    post = models.ForeignKey('Post')
    picture = ImageField(upload_to="%Y/%m/%d",blank=True,null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.post.pk) + ' ' + self.post.title
