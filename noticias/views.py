from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/lista.html', {'noticias': noticias})

def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})