# Generated by Django 4.0.4 on 2022-09-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='latest_blog',
            field=models.BooleanField(default=False, verbose_name='latest_blog'),
        ),
    ]
