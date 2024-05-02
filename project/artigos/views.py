from django.shortcuts import render
from .models import Article, Comment

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'artigos/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    return render(request, 'artigos/article_detail.html', {'article': article, 'comments': comments})