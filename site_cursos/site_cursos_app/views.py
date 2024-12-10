from django.shortcuts import render,redirect
from .models import Aluno
from django.contrib.sessions.backends.db import SessionStore
from .serviceclasses import ServicoCurso
# Create your views here.

def login(request):
   if request.method == "POST": #clicou no botão
         name = request.POST.get("name")
         email = request.POST.get("email")
         password = request.POST.get("password")

         alunos = Aluno.objects.filter(
            email=email,
            senha=password
         )

         aluno: Aluno
         if len(alunos) > 1:
            print("-- Achou mais de um Aluno com mesmo login, teve problema ---")
         elif len(alunos) == 0: #nenhum aluno igual
            print("---- Criando Novo Aluno ----")
            aluno = Aluno.objects.create(
                nome=name,
                senha=password,
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
   return render(request,"dashboard.html")

def course_search(request):
    query = request.GET.get('query', '').strip()
    Servico = ServicoCurso()
    cursos:list = Servico.GetCursosNome(query) if query else []

    for curso in cursos:
        for modulo in curso.modulos.all(): 
            print(modulo.nome)

    return render(request,"course_search.html",{
        'query': query,
        'courses': cursos
    })