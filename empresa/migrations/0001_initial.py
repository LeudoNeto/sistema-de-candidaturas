# Generated by Django 4.0.6 on 2022-08-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id_vaga', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('faixa_salarial', models.IntegerField()),
                ('escolaridade', models.CharField(max_length=50)),
                ('nome_da_empresa', models.CharField(max_length=255)),
                ('email_da_empresa', models.CharField(max_length=255)),
            ],
        ),
    ]
