# Generated by Django 3.1.4 on 2020-12-31 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0009_auto_20201231_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='category',
            field=models.CharField(choices=[('Support', 'Support'), ('Implementation', 'Implamentation'), ('Assessment', 'Assessment'), ('Outsourcing', 'Outsourcing')], default='Support', max_length=50, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
