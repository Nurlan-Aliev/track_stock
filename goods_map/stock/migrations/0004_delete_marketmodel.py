# Generated by Django 4.2.4 on 2023-08-21 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_marketmodel_name_alter_stockmodel_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MarketModel',
        ),
    ]