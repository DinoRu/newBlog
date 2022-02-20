from operator import mod
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS = [
    ('R', 'Rediger'),
    ('P', 'Publier'),
]



class Article(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    contenu = RichTextField(blank=True, null=True)
    # contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=STATUS, default='Rediger')
    category = models.CharField(max_length=255, default='Python')
    likes = models.ManyToManyField(User, related_name='blog_article')

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('blog:home')

    def total_like(self):
        return self.likes.count()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:home')

                 
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.article.titre, self.name)


