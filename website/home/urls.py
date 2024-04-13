from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('create-article', views.CreateArticleView.as_view(), name='create_article')
]
