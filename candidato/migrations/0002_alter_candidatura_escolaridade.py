# Generated by Django 4.0.6 on 2022-08-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatura',
            name='escolaridade',
            field=models.IntegerField(),
        ),
    ]
