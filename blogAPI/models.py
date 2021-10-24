from django.db import models
import uuid
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog_post_detail', args=[self.slug])
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # email = models.EmailField(max_length=75)
    # website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    # post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=None)
    post_id = models.UUIDField()
    author = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.author + '_comment'

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.author + '_comment'
