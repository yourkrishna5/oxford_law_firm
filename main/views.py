from django.shortcuts import render
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"
        
        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["oxfordlawfirm5@gmail.com"],
            fail_silently=False,
        )
        return redirect("contact_success")
    
    return render(request, "contact.html")

def contact_success(request):
    return render(request, "contact_success.html")


# ------------------------
# Team Members
# ------------------------
def team_view(request):
    members = TeamMember.objects.all()
    return render(request, "team.html", {"members": members})


# ------------------------
# Articles / Blogs
# ------------------------
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "article_list.html", {"articles": articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article_detail.html", {"article": article})


# ------------------------
# Notices
# ------------------------
def notice_list(request):
    notices = Notice.objects.filter(is_active=True).order_by("-published_at")
    return render(request, "notice_list.html", {"notices": notices})