# Generated by Django 3.1.4 on 2020-12-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20201211_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
