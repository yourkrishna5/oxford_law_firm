from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Remove contact page URL from website
    path('contact', views.contact, name='contact_email'),
   

    # Team
    path('team/', views.team_view, name='team'),

    # Articles
    path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Notices
    path('notices/', views.notice_list, name='notices'),
]