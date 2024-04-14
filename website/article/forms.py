from django.forms import ModelForm
from home.models import Post

class ArticleForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'text']