from django.urls import path
from .views import AddBlog


urlpatterns = [
    path('create/', AddBlog.as_view(), name='add_blogs'),
]
