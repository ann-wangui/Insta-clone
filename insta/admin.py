from django.contrib import admin
from django.contrib import admin
from .models import  Profile, Post, Comment, Follow

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
