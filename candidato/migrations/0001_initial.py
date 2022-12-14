# Generated by Django 4.0.6 on 2022-08-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id_candidatura', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_vaga', models.IntegerField()),
                ('nome_da_empresa', models.CharField(max_length=255)),
                ('nome_da_vaga', models.CharField(max_length=255)),
                ('nome_do_candidato', models.CharField(max_length=255)),
                ('email_do_candidato', models.CharField(max_length=255)),
                ('pretensao_salarial', models.IntegerField()),
                ('experiencia', models.TextField()),
                ('escolaridade', models.CharField(max_length=50)),
            ],
        ),
    ]
