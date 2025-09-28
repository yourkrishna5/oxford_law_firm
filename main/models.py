from django.db import models

# Team members
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="team_photos/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Articles / Blogs
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # for SEO-friendly URLs
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="article_images/", blank=True, null=True)

    def __str__(self):
        return self.title


# Notices
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title