# Generated by Django 5.0.6 on 2024-06-04 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
    ]