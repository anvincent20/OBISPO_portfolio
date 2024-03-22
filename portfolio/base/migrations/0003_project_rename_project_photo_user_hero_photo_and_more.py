# Generated by Django 5.0.1 on 2024-03-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_project_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showcase_title', models.CharField(blank=True, max_length=200, null=True)),
                ('showcase_description', models.CharField(blank=True, max_length=200, null=True)),
                ('project_photo', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='project_photo',
            new_name='hero_photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shwocase_title',
        ),
        migrations.AddField(
            model_name='user',
            name='about_photo',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
