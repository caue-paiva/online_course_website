from django.shortcuts import render,redirect
from .models import Aluno
from django.contrib.sessions.backends.db import SessionStore
from .serviceclasses import ServicoAluno
# Create your views here.

def login(request):
   if request.method == "POST": #clicou no botão
         nome = request.POST.get("name")
         email = request.POST.get("email")
         senha = request.POST.get("password")

         alunos = Aluno.objects.filter(
            email=email,
            senha=senha
         )

         aluno: Aluno
         if len(alunos) > 1:
            print("-- Achou mais de um Aluno com mesmo login, teve problema ---")
         elif len(alunos) == 0: #nenhum aluno igual
            print("---- Criando Novo Aluno ----")
            aluno = Aluno.objects.create(
                nome=nome,
                senha=senha,
                email=email
            )
         else:
            aluno = alunos[0]
            print("-- Aluno já Existia ---")
         
         request.session["user_id"] = aluno.id #guarda os dados do login na sessão
         request.session["user_name"] = aluno.nome
         request.session["user_email"] = aluno.email
         
         return redirect("dashboard")  # Redirect to the dashboard view

   return render(request, "login.html")

def dashboard(request):
   servico = ServicoAluno()

   #pega os dados da sessão do user
   id_usuario = request.session.get("user_id")
   nome_usuario = request.session.get("user_name")
   email_usuario = request.session.get("user_email")
   if id_usuario is None:
      print("-- Usuario Não autenticado --")
      raise RuntimeError("Usuario Não autenticado")
   
   #tenta desinscrever de um curso
   if request.method == "POST":
      id_curso = int(request.POST.get("curso_id"))
      print(id_curso)
      if not servico.CancelarInscricao(id_usuario,id_curso):
         print("Falha ao desinscrever aluno do curso, o aluno não existe")
      else:
         print("Operação de desinscrever teve sucesso")

   #renderiza dashboard
   cursos = servico.CursosDoUsuario(int(id_usuario))
   return render(request,"dashboard.html",{
       "username": nome_usuario,
       "user_email": email_usuario,
       "courses": cursos
   })

def course_search(request):
   Servico = ServicoAluno()

   if request.method == "POST":
      id_usuario = request.session.get("user_id")
      id_curso = request.POST.get("curso_id")
      print("--- Vars:  ",id_usuario,id_curso,"  ---")
        
      if id_usuario is None:
            print("-- Usuario Não autenticado --")
            raise RuntimeError("Usuario Não autenticado")
      if id_curso is None:
            print("-- Curso Não Encontrado --")
            raise RuntimeError("-- Curso Não Encontrado --")

      Servico.InscreverCurso(
            id_usuario = int(id_usuario),
            id_curso = int(id_curso)
      )
   
   query = request.GET.get('query', '').strip()
   cursos:list = Servico.GetCursosNome(query) if query else []
   for curso in cursos:
         for modulo in curso.modulos.all(): 
               print(modulo.nome)
   return render(request,"course_search.html",{
         'query': query,
         'courses': cursos
   })