# Generated by Django 3.1.2 on 2020-10-14 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='Full name')),
                ('birth_year', models.SmallIntegerField(verbose_name='birth year')),
                ('country', models.CharField(max_length=2, verbose_name='country')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='Full name')),
                ('birth_year', models.SmallIntegerField(verbose_name='Birth_year')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Publishing name')),
                ('location', models.CharField(max_length=2, verbose_name='Location')),
                ('owner', models.TextField(verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, verbose_name='International standard of the "books number"')),
                ('title', models.TextField(verbose_name='Book title')),
                ('description', models.TextField(verbose_name='Description')),
                ('year_release', models.SmallIntegerField(verbose_name='Year release')),
                ('copy_count', models.SmallIntegerField(default=1, verbose_name='Copy count')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Price')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='p_library.author', verbose_name='Author')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='p_library.publisher', verbose_name='Publishing house')),
                ('reader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_reader', to='p_library.friend', verbose_name='Reader')),
            ],
        ),
    ]
