# Generated by Django 5.0.6 on 2024-05-16 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0028_remove_comment_any_user_alter_comment_user'),
        ('members', '0015_alter_userprofile_about_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='members.userprofile'),
        ),
    ]