from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField(max_length=300)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    publicada = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo
