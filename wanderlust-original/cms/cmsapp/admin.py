from django.contrib import admin
from .models import *


class PostAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


class CategoryAd (admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_title',)}




admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAd)
admin.site.register(Comment)
admin.site.register(Contact)
