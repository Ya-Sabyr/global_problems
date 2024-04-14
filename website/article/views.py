from django.views.generic import CreateView
from home.models import Post
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'article/create-article.html'
    
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home')
    success_url = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to the login page
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)