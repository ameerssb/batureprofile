# Generated by Django 4.1.5 on 2023-06-01 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_project_tools'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tools',
            new_name='requirement',
        ),
    ]
