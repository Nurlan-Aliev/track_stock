# Generated by Django 4.2.3 on 2023-07-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_rename_prise_goodsmodel_cost_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsmodel',
            name='cost_price',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]