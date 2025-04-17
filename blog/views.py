# Import the render function to render HTML templates with context
from django.shortcuts import render

# Import get_object_or_404 to retrieve a specific object or return a 404 error if not found
from django.shortcuts import get_object_or_404

# Import the Blog model to interact with the blog posts in the database
from .models import Blog

# Import requests to make HTTP requests (used to fetch country data from an external API)
import requests

# Define the view for the blog list page
def blog_list(request):
    # Fetch all blog posts from the database
    blogs = Blog.objects.all()

    # Initialize an empty list to store country data
    countries = []

    # Try to fetch country data from the external API (RestCountries)
    try:
        # Make an HTTP GET request to the RestCountries API to fetch all countries
        response = requests.get("https://restcountries.com/v3.1/all")
        
        # If the response is successful (status code 200), parse the JSON data
        if response.status_code == 200:
            countries = response.json()
    # Handle any exceptions (e.g., connection errors, invalid response, etc.)
    except:
        pass

    # Render the 'blog_list.html' template with the blogs and countries data passed as context
    return render(request, "blog/blog_list.html", {"blogs": blogs, "countries": countries})

# Define the view for the blog detail page
def blog_detail(request, pk):
    # Retrieve the specific blog post based on the primary key (pk), or return a 404 error if not found
    blog = get_object_or_404(Blog, pk=pk)
    
    # Render the 'blog_detail.html' template with the specific blog data passed as context
    return render(request, "blog/blog_detail.html", {"blog": blog})
