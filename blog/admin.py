from django.contrib import admin

from .models import Author, Categories, Post, Topics


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(Categories)
admin.site.register(Topics)
admin.site.register(Post)
