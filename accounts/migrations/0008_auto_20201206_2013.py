# Generated by Django 3.1.3 on 2020-12-06 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201204_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='category',
        ),
        migrations.AddField(
            model_name='parentcompany',
            name='category',
            field=models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronce', 'Bronce')], help_text='Required', max_length=10, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='parentcompany',
            name='name',
            field=models.CharField(help_text='Required', max_length=64, unique=True, verbose_name='Name'),
        ),
    ]