from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.team_view, name="team"),
    path("articles/", views.article_list, name="article_list"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("notices/", views.notice_list, name="notice_list"),
]