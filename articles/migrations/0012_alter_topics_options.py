# Generated by Django 3.2.8 on 2022-03-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20220328_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topics',
            options={'ordering': ['article'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематика статей'},
        ),
    ]
