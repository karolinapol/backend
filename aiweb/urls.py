from django.urls import path
from .views import indexArticleJson


urlpatterns = [
    path('data/', indexArticleJson),
]