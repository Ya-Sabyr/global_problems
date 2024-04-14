from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('article/<int:pk>', views.PostView.as_view(), name='article'),
]
