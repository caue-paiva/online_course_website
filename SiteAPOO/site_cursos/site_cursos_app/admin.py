from django.contrib import admin
from .models import Aluno,Curso,Modulo
# Register your models here.

admin.site.register(Aluno) #para aparecer esses Modelos no painel de Admin do Django
admin.site.register(Curso)
admin.site.register(Modulo)