from django.urls import path
from . import views

app_name = 'noticias'


urlpatterns = [
    path('<int:ano>/<int:mes>/<int:dia>/', views.noticias_por_dia, name='noticias_por_dia'),
]