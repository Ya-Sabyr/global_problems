from django.views.generic import ListView, TemplateView, CreateView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'home/home.html'


class PostView(TemplateView):
    pass

class CreateArticleView(CreateView):
    pass