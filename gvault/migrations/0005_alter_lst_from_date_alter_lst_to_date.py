# Generated by Django 4.1 on 2022-08-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvault', '0004_lst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lst',
            name='From_Date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lst',
            name='To_Date',
            field=models.CharField(max_length=10),
        ),
    ]
