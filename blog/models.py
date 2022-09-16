from django.db import models

# Create your models here.

class Postagem (models.Model):
    titulo = models.CharField (max_length=80)
    conteudo = models.TextField ()
    data_publicacao = models.DateField (auto_now_add=True)