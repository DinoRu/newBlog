from django.contrib import admin
from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'slug', 'date_creation', 'status']
    list_filter =  ['date_creation', 'status']
    prepopulated_fields = {'slug': ('titre', )}
    search_fields = ['titre']
    

