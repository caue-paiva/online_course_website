from .ServicoCurso import ServicoCurso
from ..models import Curso, Aluno

class ServicoUsuario():
   __servico_curso = ServicoCurso()

   def __CursosDoUsuarioIDs(self,id_usuario:int)->list[int]:
      """
      Retorna os IDs dos cursos que o usuario está inscrito em.

      Return
         (list[int]): lista de IDs  dos cursos que o usuario está inscrito
      """
      try:
         aluno = Aluno.objects.get(id=id_usuario) #query no aluno do id
         lista_cursos:list = aluno.ListaCursosInscritos #pega lista de cursos e dá append
         return lista_cursos #retorna true de qualquer jeito, pq no final ele vai estar inscrito no curso certo
      except Aluno.DoesNotExist:
        return False
   
   def CursosDoUsuario(self,id_usuario:int)->list[Curso]:
      """
      Retorna os objetos cursos que o usuario está inscrito em.

      Return
         (list[Curso]): lista de objetos dos cursos que o usuario está inscrito"""
      return self.__servico_curso.GetCursos(
         self.__CursosDoUsuarioIDs(id_usuario)
      )

   def InscreverCurso(self,id_usuario:int,id_curso:int)->bool:
      """
      Inscreve um aluno num curso (dado o id de ambos)
      
      Return:
         (bool): True se o aluno existe e a operação teve sucesso, False se ele não existe e/ou deu erro na query
      """
      try:
         aluno = Aluno.objects.get(id=id_usuario) #query no aluno do id
         lista_cursos:list = aluno.ListaCursosInscritos #pega lista de cursos e dá append
        
         if id_curso not in lista_cursos: #curso não tem na lista
            lista_cursos.append(id_curso)
            aluno.ListaCursosInscritos = lista_cursos
            aluno.save() # salva no BD
         
         return True #retorna true de qualquer jeito, pq no final ele vai estar inscrito no curso certo
      except Aluno.DoesNotExist:
        return False

   def CancelarInscricao(self,id_usuario:int,id_curso:int)->bool:
      """
      Desinscreve um aluno num curso (dado o id de ambos)

      Return:
         (bool): True se o aluno existe e a operação teve sucesso, False se ele não existe e/ou deu erro na query
      """
      try:
         aluno = Aluno.objects.get(id=id_usuario) #query no aluno do id
         lista_cursos:list = aluno.ListaCursosInscritos #pega lista de cursos e dá append
        
         if id_curso in lista_cursos: #curso não tem na lista
            lista_cursos.remove(id_curso)
            aluno.ListaCursosInscritos = lista_cursos
            aluno.save() # salva no BD
         
         return True #retorna true de qualquer jeito, pq no final ele vai NÃO estar inscrito no curso certo
      
      except Aluno.DoesNotExist: #false pq o aluno não existe
        return False

   def GetCurso(self,id_curso:int)->Curso|None:
      return self.__servico_curso.GetCurso(id_curso)
      
   def GetCursosNome(self,nome:str)->list[Curso]:
      return self.__servico_curso.GetCursosNome(nome)

   def GetCursos(self,ids_curso:list[int])->list[Curso]:
      return self.__servico_curso.GetCursos(ids_curso)
   


