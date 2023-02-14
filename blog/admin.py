from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):  # Configuracion Extendida
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username')
    date_hierarchy='published'

admin.site.register(Blog, BlogAdmin)