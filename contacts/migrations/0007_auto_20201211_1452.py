# Generated by Django 3.1.4 on 2020-12-11 17:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20201206_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='Required', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
