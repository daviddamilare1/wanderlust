# Generated by Django 5.0.4 on 2024-05-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0013_comment_picture_alter_comment_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='picture',
        ),
    ]
