# Generated by Django 4.1.4 on 2022-12-08 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_remove_order_m20_remove_order_m30_remove_order_m40_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Order",),
    ]