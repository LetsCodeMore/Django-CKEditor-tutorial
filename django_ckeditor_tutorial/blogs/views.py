from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import BlogForm
from .models import BlogPost


class AddBlog(SuccessMessageMixin, CreateView):
    form_class = BlogForm
    model = BlogPost
    template_name = "blogs/add_blogs.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('add_blogs')
