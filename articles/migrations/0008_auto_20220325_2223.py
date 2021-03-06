# Generated by Django 3.2.8 on 2022-03-25 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20220325_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.section', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
    ]
