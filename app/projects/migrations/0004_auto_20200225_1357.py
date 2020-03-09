# Generated by Django 3.0.2 on 2020-02-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200225_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_apr',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_aug',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_dec',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_feb',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_jan',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_jul',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_jun',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_mar',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_may',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_nov',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_oct',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='yearlyworkload',
            name='workload_sep',
            field=models.PositiveIntegerField(),
        ),
    ]