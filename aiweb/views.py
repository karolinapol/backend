from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Article


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')