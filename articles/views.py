from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.


def article_list(request):
    article = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles': article})


def article_details(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/account/login/")
def article_create(request):
    if(request.method == 'POST'):
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            inst = form.save(commit=False)
            inst.author = request.user
            inst.save()
            return redirect("articles:list")

    else:
        form = forms.CreateArticle()
        return render(request, "articles/article_create.html", {'form': form})


@login_required(login_url="/account/login/")
def article_delete(request, id):
    article = Article.objects.get(id=id)
    if article.author != request.user:
        return redirect("articles:list")
    article.delete()
    return redirect("articles:list")
