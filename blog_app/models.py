# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user, via the User model in the auth app
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    # identify when post was created 
    created_date = models. DateTimeField(auto_now_add=True) 
    # we can choose not to publish a blog post immediately
    published_date = models.DateTimeField(blank=True, null=True) 

    # function we can call to update our database
    # when we do decide to our blog entry
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # set blog title as the identifier for each blog post instance
    def __unicode__(self):
        return self.title
