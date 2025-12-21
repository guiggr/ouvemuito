from django.db import models

class Noticia(models.Model):
    subtitulo = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Subtítulo'
    )
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data_publicacao.strftime('%d/%m/%Y')