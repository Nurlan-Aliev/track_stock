# Generated by Django 4.2.3 on 2023-07-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_goodsmodel_cost_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsmodel',
            name='cost_price',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
