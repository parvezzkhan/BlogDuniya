# Generated by Django 5.0 on 2024-01-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Duniya!', max_length=255),
        ),
    ]
