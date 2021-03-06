# Generated by Django 3.1.4 on 2020-12-12 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_parentcompany_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parentcompany',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='account',
            name='parent_company',
            field=models.ForeignKey(help_text='Required', on_delete=django.db.models.deletion.PROTECT, related_name='parent_company', to='accounts.parentcompany'),
        ),
    ]
