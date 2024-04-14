from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateArticleView.as_view(), name='create_article'),
]
