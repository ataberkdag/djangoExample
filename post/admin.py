from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'publishDate']
    list_display_links = ['title', 'publishDate']
    list_editable = ['summary']
    list_filter = ['publishDate']
    search_fields = ['title', 'summary', 'content']

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)