# Generated by Django 4.2.3 on 2023-08-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_alter_countgoods_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countgoods',
            name='datetime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
