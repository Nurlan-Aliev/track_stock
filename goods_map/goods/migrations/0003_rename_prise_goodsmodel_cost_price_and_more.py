# Generated by Django 4.2.3 on 2023-07-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goodsmodel_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsmodel',
            old_name='prise',
            new_name='cost_price',
        ),
        migrations.AddField(
            model_name='goodsmodel',
            name='retail_price',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsmodel',
            name='weight',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsmodel',
            name='wholesale_price',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]