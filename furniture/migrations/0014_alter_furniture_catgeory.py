# Generated by Django 4.0.1 on 2022-04-24 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('furniture', '0013_remove_woodinformation_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='catgeory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projecttypes'),
        ),
    ]
