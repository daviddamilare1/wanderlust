# Generated by Django 5.0.4 on 2024-05-11 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0012_remove_comment_picture'),
        ('members', '0014_alter_userprofile_about_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.userprofile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
