# Generated by Django 4.0.1 on 2022-04-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_delete_post_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kul_ad', models.CharField(max_length=150)),
                ('about_user', models.TextField()),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]