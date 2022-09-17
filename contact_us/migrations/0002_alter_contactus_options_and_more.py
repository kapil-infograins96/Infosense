# Generated by Django 4.0.4 on 2022-09-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Infograins'},
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='projectDescription',
        ),
        migrations.AddField(
            model_name='contactus',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(default='', help_text='MESSAGE', verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='regionName',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='regionName'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.TextField(blank=True, default='', null=True, verbose_name='subject'),
        ),
    ]