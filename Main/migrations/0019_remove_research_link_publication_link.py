# Generated by Django 4.1.5 on 2023-06-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_research_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='link',
        ),
        migrations.AddField(
            model_name='publication',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
