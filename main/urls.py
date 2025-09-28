from django.urls import path
from . import views

urlpatterns = [
    # Static pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),

    # Team
    path('team/', views.team_view, name='team'),

    # Articles
    path('articles/', views.article_list, name='article_list'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Notices
    path('notices/', views.notice_list, name='notice_list'),
]