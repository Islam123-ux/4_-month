from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'rate']
   list_filter = ['created_at', 'updated_at']
   search_fields = ['title', 'content']