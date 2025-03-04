# Generated by Django 3.0.5 on 2020-10-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volton', '0006_auto_20201005_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='titlesite',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title'),
        ),
        migrations.AddField(
            model_name='blogtr',
            name='titlesite',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Başlık'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='blogtr',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık'),
        ),
    ]
