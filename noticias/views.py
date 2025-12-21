from django.shortcuts import render, get_object_or_404
from .models import Noticia
from django.utils.timezone import now

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/lista.html', {'noticias': noticias})

def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})

def noticias_do_dia(request):
    hoje = now().date()  
    noticias = Noticia.objects.filter(
        data_publicacao__date=hoje,
        publicada=True
    )

    return render(request, 'noticias/por_dia.html', {
        'data': hoje,
        'noticias': noticias
    })