# Generated by Django 4.1.4 on 2022-12-07 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_list_age_and_gender"),
    ]

    operations = [
        migrations.DeleteModel(name="Bill",),
    ]
