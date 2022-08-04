from django.db import models

# Create your models here.
class Vaga(models.Model):
    id_vaga = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    faixa_salarial = models.IntegerField()
    escolaridade = models.IntegerField()
    nome_da_empresa = models.CharField(max_length=255)
    email_da_empresa = models.CharField(max_length=255)