# Generated by Django 3.1.3 on 2020-12-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201204_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['status']},
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('Client', 'Client'), ('Prospect', 'Prospect'), ('Former Client', 'Former Client')], default='Prospect', help_text='Required', max_length=15, verbose_name='Status'),
        ),
    ]