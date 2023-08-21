# Generated by Django 4.2.4 on 2023-08-21 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_marketmodel_name_alter_stockmodel_name'),
        ('goods', '0025_goodsmodel_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsmodel',
            name='market',
        ),
        migrations.AddField(
            model_name='goodsmodel',
            name='market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='market', to='stock.marketmodel'),
        ),
    ]
