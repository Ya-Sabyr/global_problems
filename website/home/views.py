from django.views.generic import ListView, DetailView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'home/home.html'


class PostView(DetailView):
    model = Post
    template_name = 'home/article-view.html'