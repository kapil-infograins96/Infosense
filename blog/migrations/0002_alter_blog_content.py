# Generated by Django 4.0.4 on 2022-09-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='blogContent'),
        ),
    ]
