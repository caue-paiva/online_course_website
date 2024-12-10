from django.db import models


# Create your models here.

class Usuario(models.Model): #classe abstrata
   nome = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   senha = models.CharField(max_length=20)
   ativo = models.BooleanField(default=True)
   ListaCursosInscritos = models.JSONField(blank=True, default=list) #lista de cursos guardado como JSON 
   
   
   class Meta: #fala pro django que a classe é abstrata
      abstract = True #o Django pede que vc faça isso eu acho

class Aluno(Usuario):
   pass


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    professor = models.CharField(max_length=50)
    #o campos de Lista de cursos é criado pelo django com uma referência de Foreign Key
    #na classe módulo

class Modulo(models.Model):
   nome = models.CharField(max_length=50) 
   #referência para o curso que cada módulo pertence (Foreign Key)
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="modulos")

   """
   não vamos colocar os atibutos de lista video aulas
   e lista textos nessa classe pois a implementação do projeto não inclui as aulas e textos 
   de cada módulo, apenas mostrar o curso e o nome de seus módulos na dashboard   
   """