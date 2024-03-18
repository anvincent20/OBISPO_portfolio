from django.forms import ModelForm
from .models import *

class PeronalInfoForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
             'middle_name',
              'greeting_description',
               'shwocase_title',
                'project_photo',
                 'last_name',
                  'contact_number',
                   'age',
                    'address',
                     'email',
                      'facebook_link',
                       'github_link',
                        'linkedin_link',
                        'discord_link',
                        'username',
                        'password',
                        'confirm_password',
                        'about_me_context',

                        
        ]