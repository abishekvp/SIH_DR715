# Generated by Django 4.1 on 2022-08-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvault', '0005_alter_lst_from_date_alter_lst_to_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lst',
            name='eligibility',
            field=models.TextField(default='National'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lst',
            name='grant_type',
            field=models.CharField(default='National', max_length=15),
        ),
        migrations.AddField(
            model_name='lst',
            name='investment',
            field=models.CharField(default='1,00,000', max_length=10),
        ),
    ]
