# Generated by Django 3.2.10 on 2022-06-05 14:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0003_rename_comments_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Post',
        ),
    ]
