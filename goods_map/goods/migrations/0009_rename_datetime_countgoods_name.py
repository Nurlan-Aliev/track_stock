# Generated by Django 4.2.3 on 2023-08-01 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_countgoods'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countgoods',
            old_name='datetime',
            new_name='name',
        ),
    ]
