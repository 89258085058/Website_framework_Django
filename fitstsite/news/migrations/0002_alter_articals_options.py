# Generated by Django 4.0 on 2021-12-14 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articals',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
