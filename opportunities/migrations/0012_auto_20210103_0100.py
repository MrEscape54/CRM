# Generated by Django 3.1.4 on 2021-01-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_auto_20210102_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(),
        ),
    ]
