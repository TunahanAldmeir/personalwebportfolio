# Generated by Django 4.0.1 on 2022-04-10 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_rename_about_about1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='about1',
        ),
    ]