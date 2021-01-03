# Generated by Django 3.1.4 on 2020-12-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0007_auto_20201230_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'ordering': ['stage', 'priority'], 'verbose_name_plural': 'Opportunities'},
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Expected Amount'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='priority',
            field=models.CharField(choices=[('4 - Low', 'Low'), ('3 - Normal', 'Normal'), ('2 - High', 'High'), ('1 - Urgent', 'Urgent')], max_length=10, verbose_name='Priority'),
        ),
    ]
