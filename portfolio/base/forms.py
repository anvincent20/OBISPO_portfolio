from django.forms import ModelForm
from .models import *

class PeronalInfoForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'greeting_description',
            'last_name',
            'age',
            'username',
            'password',
            'confirm_password',
            'hero_photo',
        ]

class AboutMeForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'address',
            'email',
            'contact_number',
            'about_me_context',
            'about_photo',
        ]


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['showcase_title', 'showcase_description', 'project_photo']


class SocialMediaForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'facebook_link',
            'github_link',
            'linkedin_link',
            'discord_link',
        ]