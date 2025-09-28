from django.shortcuts import render, get_object_or_404
from .models import TeamMember, Article, Notice

# Team page
def team_view(request):
    members = TeamMember.objects.all()
    return render(request, "team.html", {"members": members})


# Blog / Article list
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "article_list.html", {"articles": articles})


# Blog / Article detail page
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article_detail.html", {"article": article})


# Notices
def notice_list(request):
    notices = Notice.objects.filter(is_active=True).order_by("-published_at")
    return render(request, "notice_list.html", {"notices": notices})