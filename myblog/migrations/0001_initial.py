# Generated by Django 5.1 on 2024-08-26 09:58

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('url', models.SlugField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
