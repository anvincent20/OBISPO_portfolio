from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name=models.CharField(max_length=200, null = True, blank = True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    greeting_description = models.CharField(max_length=200, null=True, blank=True)
    shwocase_title = models.CharField(max_length=200, null=True, blank=True)
    project_photo = models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null = True, blank=True)
    contact_number=models.CharField(max_length=200, null = True, blank=True)
    age = models.CharField(max_length=200, null = True, blank=True)
    address = models.CharField(max_length=200, null = True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    facebook_link=models.CharField(max_length=200, null = True, blank=True)
    github_link=models.CharField(max_length=200, null = True, blank=True)
    linkedin_link=models.CharField(max_length=200, null = True, blank=True)
    discord_link=models.CharField(max_length=200, null = True, blank=True)
    username = models.CharField(max_length=150,null = True, blank=True, unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirm_password = models.CharField(max_length=200, null=True, blank=True)
    about_me_context=models.CharField(max_length=200, null = True, blank = True)

    def str(self):
        return self.email or str(self.id)