# sitemap.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article, Notice, TeamMember


# 🔹 For static pages (home, about, contact, team)
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ["home", "about", "contact", "team"]

    def location(self, item):
        return reverse(item)


# 🔹 For Articles (blogs)
class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


# 🔹 For Notices
class NoticeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Notice.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.published_at


# 🔹 For Team Members (optional: if you have detail pages)
class TeamMemberSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return TeamMember.objects.all()

    # Only add this if you have a detail view like team_member_detail
    # def location(self, obj):
    #     return reverse("team_member_detail", args=[obj.id])