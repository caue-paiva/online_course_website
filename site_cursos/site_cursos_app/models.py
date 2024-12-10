from django.db import models
from abc import ABC,abstractmethod

# Create your models here.

class Usuario(models.Model,ABC): #classe abstrata
   

   class Meta:
      abstract = True #o Django pede que vc faça isso eu acho

class Aluno(Usuario):
   pass #herda de usuário