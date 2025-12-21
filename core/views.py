from django.shortcuts import render
from noticias.models import Noticia

def home(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-data_publicacao')
    return render(request, 'core/home.html', {
        'noticias': noticias
    })