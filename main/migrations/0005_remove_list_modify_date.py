# Generated by Django 4.1.4 on 2022-12-08 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_delete_order"),
    ]

    operations = [
        migrations.RemoveField(model_name="list", name="modify_date",),
    ]