# Generated by Django 4.1.7 on 2023-03-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TboProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectlocations',
            name='finValue',
            field=models.IntegerField(null=True, verbose_name='finValue'),
        ),
        migrations.AlterField(
            model_name='objectlocations',
            name='oktmo',
            field=models.IntegerField(null=True, verbose_name='oktmo'),
        ),
        migrations.AlterField(
            model_name='objectlocations',
            name='scaleMap',
            field=models.IntegerField(null=True, verbose_name='scaleMap'),
        ),
    ]
