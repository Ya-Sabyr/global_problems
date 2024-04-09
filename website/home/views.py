from django.views.generic import ListView, TemplateView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'home/home.html'


class PostView(TemplateView):
    pass