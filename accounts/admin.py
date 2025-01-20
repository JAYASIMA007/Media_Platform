# filepath: /d:/project/project/accounts/admin.py
from django.contrib import admin
from .models import UserProfile, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)

admin.site.register(UserProfile)