# Generated by Django 4.1 on 2022-08-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regextend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_type', models.CharField(max_length=10)),
                ('orgname', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('profile_pic', models.BinaryField()),
            ],
        ),
    ]
