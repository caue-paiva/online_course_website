from ..models import Curso
from django.db.models.functions import Lower, Replace
from django.db.models import Value
import re

class ServicoCurso():  
   def InscreverCurso(self,id_usuario:int,id_curso:int)->bool:
      pass

   def CancelarInscricao(self,id_usuario:int,id_curso:int)->bool:
      pass

   def GetCurso(self,id_curso:int)->Curso|None:
      try:
        return Curso.objects.get(id=id_curso)
      except Curso.DoesNotExist:
        return None

   def GetCursosNome(self,nome:str)->list[Curso]:
      nome_filtrado = re.sub(r'\s+', ' ', nome).strip().lower()
      
      cursos = Curso.objects.annotate(
        normalized_name=Lower(Replace('nome', Value(' '), Value('')))
      ).filter(normalized_name__icontains=nome_filtrado).prefetch_related('modulos')

      return list(cursos)

   def GetCursos(self,ids_curso:list[int])->list[Curso]:
      return list(Curso.objects.filter(id__in=ids_curso))


