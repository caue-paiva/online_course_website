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
                if not Curso.objects.exists():
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
                        professor="Tuezin"
                    )
                    Modulo.objects.create(nome="Introdução ao Django", curso=curso2)
                    Modulo.objects.create(nome="MVC no Django", curso=curso2)
            except OperationalError:
                pass
        post_migrate.connect(populate_db, sender=self) #só executa a função depois do Migrate, mais safe