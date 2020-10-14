from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField(verbose_name='Full name')
    birth_year = models.SmallIntegerField(verbose_name='birth year')
    country = models.CharField(verbose_name='country' ,max_length=2)

    def __str__(self):
        return self.full_name


class Friend(models.Model):
    full_name = models.TextField(verbose_name='Full name')
    birth_year = models.SmallIntegerField(verbose_name='Birth_year')

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField(verbose_name='Publishing name')
    location = models.CharField(max_length=2, verbose_name='Location')
    owner = models.TextField(verbose_name='Owner')

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(verbose_name='International standard of the "books number"', max_length=13)
    title = models.TextField(verbose_name='Book title')
    description = models.TextField(verbose_name='Description')
    year_release = models.SmallIntegerField(verbose_name='Year release')
    copy_count = models.SmallIntegerField(verbose_name='Copy count', default=1)
    price= models.DecimalField(verbose_name='Price', max_digits=6, decimal_places=2, default=0)
    publisher = models.ForeignKey('p_library.Publisher', null=True, blank=True, verbose_name='Publishing house',
                                         on_delete=models.CASCADE, related_name='book_publisher')
    author = models.ForeignKey('p_library.Author', verbose_name='Author', on_delete=models.CASCADE,
                               related_name='book_author')
    reader = models.ForeignKey('p_library.Friend', null=True, blank=True, verbose_name='Reader',
                                     on_delete=models.CASCADE, related_name='book_reader')

    def __str__(self):
        return self.title


