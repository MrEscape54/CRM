# Generated by Django 3.1.4 on 2021-01-16 16:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0019_auto_20210104_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ParentCompany',
            new_name='ParentAccount',
        ),
    ]
