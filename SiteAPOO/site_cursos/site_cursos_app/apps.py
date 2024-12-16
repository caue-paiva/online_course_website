from django.apps import AppConfig
from django.db.utils import OperationalError



class SiteCursosAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_cursos_app'

    def ready(self): #verifica se tem dados de ilustração no BD
        from site_cursos_app.models import Curso, Modulo #tem que importar aqui mesmo, senão da problema
        from django.db.models.signals import post_migrate
        
        def populate_db(sender, **kwargs): #função para popular BD se n tiver dados
            try:
                if Curso.objects.count() < 5:
                    curso1 = Curso.objects.create(
                        nome="Python para Ciência de Dados",
                        descricao="Básico de Python, curso oferecido pelo DATA.",
                        professor="Enzo"
                    )
                    Modulo.objects.create(nome="Introdução ao Python", curso=curso1)
                    Modulo.objects.create(nome="Funções no Python", curso=curso1)

                    curso2 = Curso.objects.create(
                        nome="Desenvolvimento com Django",
                        descricao="Desenvolvimento Web development com Django.",
                        professor="Matheus Brasileiro"
                    )
                    Modulo.objects.create(nome="Introdução ao Django", curso=curso2)
                    Modulo.objects.create(nome="MVC no Django", curso=curso2)

                    curso3 = Curso.objects.create(
                        nome="Introdução ao FL Studio",
                        descricao="Como começar a produzir música utilizando o famoso FL Studio.",
                        professor="João Godoy"
                    )
                    Modulo.objects.create(nome="Como baixar o FL Studio na sua máquina", curso=curso3)
                    Modulo.objects.create(nome="Conhecendo as principais funcionalidades do FL Studio", curso=curso3)

                    curso4 = Curso.objects.create(
                        nome="Primeiros Passos no mundo das criptomoedas",
                        descricao="Como começar a investir no promissor mercado de criptomoedas.",
                        professor="Ruyter"
                    )
                    Modulo.objects.create(nome="Visão geral das criptomoedas", curso=curso4)
                    Modulo.objects.create(nome="O que são as criptomoedas", curso=curso4)

                    curso5 = Curso.objects.create(
                        nome="Tópicos avançados em mecânica quântica",
                        descricao="Entenda os conceitos e ideias por trás do Nobel da Física de 2022.",
                        professor="Nikolai Fedorovich Kalinin"
                    )
                    Modulo.objects.create(nome="Entendendo os mecanismos descobertos por Alain Aspect, John Clauser e Anton Zeilinger", curso=curso5)
                    Modulo.objects.create(nome="Teoria I", curso=curso5)
                    Modulo.objects.create(nome="Teoria II", curso=curso5)
                    Modulo.objects.create(nome="Teoria III", curso=curso5)


            except OperationalError:
                pass
        post_migrate.connect(populate_db, sender=self) #só executa a função depois do Migrate, mais safe