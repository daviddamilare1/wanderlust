# Generated by Django 5.0.4 on 2024-05-11 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0011_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='picture',
        ),
    ]
