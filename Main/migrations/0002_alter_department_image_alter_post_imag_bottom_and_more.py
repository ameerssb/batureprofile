# Generated by Django 4.1 on 2022-11-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, upload_to='department_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imag_bottom',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_middle',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_top',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
    ]
