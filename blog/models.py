""" Documentation """
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    """ A manager that displays only published posts """
    def get_queryset(self):
        """ Output of published posts """
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    """ Description of the post fields """
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    tags = TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        """ Meta description of the post fields """
        ordering = ('publish',)

    def get_absolute_url(self):
        """ Getting the post url """
        return reverse('blog:post_detail', args=[self.publish.year,
                       self.publish.month, self.publish.day, self.slug])

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """ Description of the comment fields """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        """ Meta description of the comment fields """
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
