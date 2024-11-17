from django.urls import path
from article.views import show_view

urlpatterns = [
    path('user/',show_view)
]