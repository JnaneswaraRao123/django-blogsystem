# Import the base Model class from Django's ORM
from django.db import models

# Define the Blog model, which represents a blog post in the database
class Blog(models.Model):
    # Title of the blog post, limited to 200 characters
    title = models.CharField(max_length=200)

    # Main content of the blog post
    content = models.TextField()

    # Country related to the blog (could be used for API integration or categorization)
    country = models.CharField(max_length=100)

    # Author of the blog post, defaulting to 'Unknown Author' if not provided
    author = models.CharField(max_length=100, default='Unknown Author')

    # Date and time when the blog post was created; auto-filled on creation
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the object, shown in admin and shell (e.g., "Blog Title")
    def __str__(self):
        return self.title

