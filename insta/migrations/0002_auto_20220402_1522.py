# Generated by Django 3.2.10 on 2022-05-05 12:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default=20, max_length=255, verbose_name='profile_picture'),
            preserve_default=False,
        ),
    ]