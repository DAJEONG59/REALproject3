# Generated by Django 4.1.2 on 2022-11-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="memory", options={"ordering": ["-id"]},),
    ]