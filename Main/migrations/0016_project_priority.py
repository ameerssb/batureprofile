# Generated by Django 4.1.5 on 2023-06-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_project_source_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
