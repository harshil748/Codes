from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date", "isbn", "genre")
    search_fields = ("title", "author", "isbn")
    list_filter = ("genre", "publication_date")
