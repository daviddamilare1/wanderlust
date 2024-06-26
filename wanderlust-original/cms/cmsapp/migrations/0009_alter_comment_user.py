# Generated by Django 5.0.4 on 2024-05-11 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0008_comment_comment_date_comment_picture_and_more'),
        ('members', '0014_alter_userprofile_about_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='members.userprofile'),
        ),
    ]
