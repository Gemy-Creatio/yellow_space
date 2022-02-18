# Generated by Django 4.0.1 on 2022-02-18 13:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_homepage_address_ar_homepage_address_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(null=True, upload_to='background/')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('content_en', ckeditor.fields.RichTextField(max_length=255, null=True)),
                ('content_ar', ckeditor.fields.RichTextField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
