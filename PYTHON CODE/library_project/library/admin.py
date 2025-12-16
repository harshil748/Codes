from django.contrib import admin
from .models import Book, Borrower


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "genre",
        "ISBN",
        "publication_date",
        "is_available",
    )
    list_filter = ("is_available", "genre")
    search_fields = ("title", "author", "ISBN")


class BorrowerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "borrowed_book", "borrow_date", "return_date")
    list_filter = ("return_date",)
    search_fields = ("name", "email")


admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
