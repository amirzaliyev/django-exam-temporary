from django.contrib import admin

from bookstore.models import Book, Author, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
