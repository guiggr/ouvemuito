from django.contrib import path
from . import views

urlpatterns = [
    path('noticias/',views.noticias, name='noticias'),
]
