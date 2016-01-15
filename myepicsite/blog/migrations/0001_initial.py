# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.utils.timezone
import geoposition.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('picture', sorl.thumbnail.fields.ImageField(null=True, verbose_name='Загрузить картинку', upload_to='%Y/%m/%d', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='Комментарий', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(null=True, verbose_name='Дата публикации', blank=True)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'картинки',
                'verbose_name': 'картинка',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(null=True, verbose_name='Текст поста', blank=True)),
                ('tag', models.CharField(choices=[(None, 'Выбрать раздел'), ('accessories', 'Аксессуары')], max_length=50, verbose_name='Раздел')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(null=True, verbose_name='Дата публикации', blank=True)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'посты',
                'verbose_name': 'пост',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(null=True, verbose_name='Текст поста', blank=True)),
                ('slug', models.SlugField(max_length=60, verbose_name='Slug', blank=True)),
                ('tag', models.CharField(choices=[(None, 'Выбрать раздел'), ('shops', 'Mагазины'), ('cafes', 'Кафе'), ('museums', 'Музеи')], max_length=50, verbose_name='Раздел')),
                ('address', models.CharField(null=True, max_length=300, verbose_name='Адрес (сохраняется автоматически)', blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='Координаты')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(null=True, verbose_name='Дата публикации', blank=True)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'обзоры',
                'verbose_name': 'обзор',
            },
        ),
    ]
