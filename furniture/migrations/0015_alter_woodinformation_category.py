# Generated by Django 4.0.1 on 2022-05-03 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0014_alter_furniture_catgeory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woodinformation',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='furniture.category'),
        ),
    ]
