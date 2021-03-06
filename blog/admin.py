from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date')
    list_filter = ('status',)
    ordering = ('-created_date',)
    search_fields = ('title', 'content')
admin.site.register(Post, PostAdmin)