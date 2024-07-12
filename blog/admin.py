from django.contrib import admin
from .models import Category, Post, Author


# Register your models here.
# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/3dw7zeclx9wuby1gn6ztp1pd2sz9rozpcz52vu1w5lkkn3sz/tinymce/7/tinymce.min.js',
              'js/script.js',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'bio')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
