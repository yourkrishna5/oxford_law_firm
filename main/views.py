from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Article, Notice, TeamMember

def home(request):
    articles = Article.objects.all().order_by('-created_at')[:5]
    notices = Notice.objects.filter(is_active=True).order_by('-published_at')[:5]
    team_members = TeamMember.objects.all()

    context = {
        "articles": articles,
        "notices": notices,
        "team_members": team_members,
    }

    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
def team_view(request):
    members = TeamMember.objects.all()
    return render(request, "team.html", {"members": members})

def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "article_list.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article_detail.html", {"article": article})

def notice_list(request):
    notices = Notice.objects.filter(is_active=True).order_by("-published_at")
    return render(request, "notice_list.html", {"notices": notices})