# Generated by Django 4.2.4 on 2023-09-17 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'categories'},
        ),
    ]
