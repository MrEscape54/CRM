# Generated by Django 3.1.3 on 2020-12-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20201204_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(max_length=50, null=True, verbose_name='Location'),
        ),
    ]
