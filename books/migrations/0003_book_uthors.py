# Generated by Django 5.0.6 on 2024-06-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_rename_created_at_book_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uthors',
            field=models.ManyToManyField(to='books.author'),
        ),
    ]