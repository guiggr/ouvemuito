from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('data_publicacao', 'publicada')
    list_filter = ('publicada', 'data_publicacao')
    search_fields = ('conteudo',)
    list_editable = ('publicada',)