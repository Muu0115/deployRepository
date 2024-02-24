# Generated by Django 4.2.8 on 2024-02-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_delete_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthrecord',
            name='physical_condition',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='sleep_hours',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
