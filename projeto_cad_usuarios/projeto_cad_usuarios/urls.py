from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #facebook.com/dev.aprender
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')

]
