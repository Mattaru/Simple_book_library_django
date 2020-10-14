from django.contrib import admin


from p_library.models import Book, Author, Publisher, Friend


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_release', 'reader')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner')


@admin.register(Friend)
class Friend(admin.ModelAdmin):
    pass
