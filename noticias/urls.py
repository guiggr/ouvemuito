from django.urls import path
from . import views

app_name = 'noticias'


urlpatterns = [
    path('<int:ano>/<int:mes>/<int:dia>/', views.noticias_do_dia, name='noticias_do_dia'),
]