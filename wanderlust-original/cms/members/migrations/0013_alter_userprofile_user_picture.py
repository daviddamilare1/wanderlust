# Generated by Django 5.0.4 on 2024-05-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_userprofile_about_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_picture',
            field=models.ImageField(upload_to='img'),
        ),
    ]
