from django.contrib import admin
from .models import TeamMember, Article, Notice

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}  # auto-fill slug from title


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")