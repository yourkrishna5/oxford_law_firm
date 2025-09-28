from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Remove contact page URL from website
    path('contact', views.contact, name='contact'),
   

    # Team
    path('team/', views.team_view, name='team'),

    # Articles
    path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Notices
    path('notices/', views.notice_list, name='notices'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)