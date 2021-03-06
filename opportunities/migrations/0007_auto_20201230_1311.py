# Generated by Django 3.1.4 on 2020-12-30 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0006_auto_20201230_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='date_of_funding',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='EDC',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Estimated Date of Closing'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='source',
            field=models.CharField(choices=[('call', 'Call'), ('email', 'Email'), ('existing customer', 'Existing Customer'), ('vendor', 'Vendor'), ('public relations', 'Public Relations'), ('compaign', 'Campaign'), ('other', 'Other')], max_length=64, verbose_name='Source'),
        ),
    ]
