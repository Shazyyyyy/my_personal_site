# Generated by Django 3.2.3 on 2021-05-17 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
    ]
