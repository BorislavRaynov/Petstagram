from django.contrib import admin
from petstagram.common.models import Comment, Like

# Register your models here.

admin.site.register(Comment)
admin.site.register(Like)