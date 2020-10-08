from django.contrib import admin
from p_library.models import Book, Author, Publishing_house

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_release')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')

@admin.register(Publishing_house)
class PublishinHousAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner')
