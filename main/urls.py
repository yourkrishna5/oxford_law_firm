from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# ✅ Import sitemap things
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, ArticleSitemap, NoticeSitemap, TeamMemberSitemap

sitemaps_dict = {
    "static": StaticViewSitemap,
    "articles": ArticleSitemap,
    "notices": NoticeSitemap,
    "team": TeamMemberSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Remove contact page URL from website (but still in sitemap)
    path('contact', views.contact, name='contact'),

    # Team
    path('team/', views.team_view, name='team'),

    # Articles
    path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Notices
    path('notices/', views.notice_list, name='notices'),

    # ✅ Sitemap URL
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps_dict}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)