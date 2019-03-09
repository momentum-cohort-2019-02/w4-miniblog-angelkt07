from django.db import models
from django.urls import reverse #remember this is to generate URLS by reversing the URL Patterns.
import uuid

# I know this is not required, but I would like to add this to help really drill in the code.
class Topic(models.Model):
    """A way for the blog post to have a type of topic."""
    name = models.CharField(max_length=30, help_text='Enter a topic.')

    def __str__(self):
        """String for representing the Topic model"""
        return self.name

class BlogPost(models.Model):
    """ A model for the blog's posts that will be entered"""
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField('Topic', help_text='Select a topic for this post.')
    postdate = models.DateTimeField(auto_now=True)

    def display_topic(self):
        """Create a string for the topic name"""
        return ', '.join(topic.name for topic in self.topic.all()[:3])

    display_topic.short_description = 'Topic'

    def __str__(self):
        """String for BlogPost"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])

class BlogComment(models.Model):
    """Model for the inline comments that can be added to the post itself"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for the comments.')
    blogpost = models.ForeignKey('BlogPost', on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=200)
    comment_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['blogpost', 'comment_date']
    
    def __str__(self):
        """String for BlogComments"""
        return f'{self.id} ({self.blogpost.title})'


class Blogger(models.Model):
    """model for my bloggers"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """string for blogger"""
        return f'{self.last_name}, {self.first_name}'
