# Generated by Django 4.0.6 on 2022-08-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='escolaridade',
            field=models.IntegerField(),
        ),
    ]
