# Generated by Django 3.1.4 on 2020-12-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20201224_0009'),
        ('accounts', '0016_auto_20201228_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='account_contacts', to='contacts.Contact'),
        ),
    ]
