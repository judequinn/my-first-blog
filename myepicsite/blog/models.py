from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField


# Посты
class Post(models.Model):

    SECTION_CHOICES = ( (None, 'Выбрать раздел'), ('accessories', 'Аксессуары') )

    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст поста', blank=True, null=True)
    tag = models.CharField('Раздел', max_length=50, choices=SECTION_CHOICES)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Картинки
class Picture(models.Model):

    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField('Название', max_length=200)
    picture = ImageField('Загрузить картинку', upload_to="%Y/%m/%d",blank=True,null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return self.title


# Обзоры
class Review(models.Model):

    SECTION_CHOICES = ( (None, 'Выбрать раздел'),('shops', 'Mагазины'), ('cafes', 'Кафе'), ('museums', 'Музеи') )

    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст поста', blank=True, null=True)
    tag = models.CharField('Раздел', max_length=50, choices=SECTION_CHOICES)
    address = models.CharField('Адрес', max_length=300, blank=True, null=True)
    c_latitude = models.CharField('Широта', max_length=50, blank=True, null=True)
    c_longitude = models.CharField('Долгота', max_length=50, blank=True, null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
