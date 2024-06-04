# Generated by Django 5.0.6 on 2024-06-04 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_authors_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
