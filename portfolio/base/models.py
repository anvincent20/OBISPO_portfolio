from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name=models.CharField(max_length=200, null = True, blank = True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    greeting_description = models.TextField(null=True, blank=True)
    last_name=models.CharField(max_length=200, null = True, blank=True)
    contact_number=models.CharField(max_length=200, null = True, blank=True)
    age = models.CharField(max_length=200, null = True, blank=True)
    address = models.CharField(max_length=250, null = True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    facebook_link=models.CharField(max_length=200, null = True, blank=True)
    github_link=models.CharField(max_length=200, null = True, blank=True)
    linkedin_link=models.CharField(max_length=200, null = True, blank=True)
    discord_link=models.CharField(max_length=200, null = True, blank=True)
    username = models.CharField(max_length=150,null = True, blank=True, unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirm_password = models.CharField(max_length=200, null=True, blank=True)
    about_me_context=models.TextField(null = True, blank = True)
    about_photo = models.FileField(upload_to='profile/', null=True, blank=True)
    hero_photo = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name="user_project")
    showcase_title = models.CharField(max_length=200, null=True, blank=True)
    showcase_description = models.CharField(max_length=200, null=True, blank=True)
    project_photo = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.showcase_title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_imgs")
    image = models.FileField(upload_to='project_images/', null=True, blank=True)