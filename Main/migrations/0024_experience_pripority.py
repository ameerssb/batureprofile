# Generated by Django 4.1.5 on 2023-09-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0023_header_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="priority",
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]