# Import the admin module from Django's contrib package
from django.contrib import admin

# Import the Blog model from the current app's models
from .models import Blog

# Register the Blog model with the Django admin site
# This allows you to manage Blog entries through the built-in Django admin interface
admin.site.register(Blog)