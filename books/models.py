from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    year = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title


class WebSite(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    oficial_website = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
