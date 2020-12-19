# Generated by Django 3.1.3 on 2020-12-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-status']},
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('Client', 'Client'), ('Prospect', 'Prospect'), ('Ex-Client', 'Ex-Client')], default='Prospect', max_length=10, verbose_name='Status'),
        ),
    ]