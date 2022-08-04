from django.db import models

# Create your models here.
class Candidatura(models.Model):
    id_candidatura = models.BigAutoField(primary_key=True)
    id_vaga = models.IntegerField()
    nome_da_empresa = models.CharField(max_length=255)
    nome_da_vaga = models.CharField(max_length=255)
    nome_do_candidato = models.CharField(max_length=255)
    email_do_candidato = models.CharField(max_length=255)
    pretensao_salarial = models.IntegerField()
    experiencia = models.TextField()
    escolaridade = models.IntegerField()