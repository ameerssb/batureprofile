# Generated by Django 4.1.5 on 2023-09-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_alter_hint_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='url',
            field=models.CharField(default='#', max_length=250),
        ),
    ]
