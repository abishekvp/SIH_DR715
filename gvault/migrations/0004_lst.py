# Generated by Django 4.1 on 2022-08-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvault', '0003_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='lst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('From_Date', models.DateField()),
                ('To_Date', models.DateField()),
                ('doc_list', models.TextField()),
            ],
        ),
    ]
