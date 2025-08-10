from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo