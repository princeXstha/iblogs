# Generated by Django 5.0.6 on 2024-06-25 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
