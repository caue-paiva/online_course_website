from django.urls import path
from . import views

urlpatterns = [
   path("",views.login,name="login"),
   path("dashboard/",views.dashboard,name="dashboard"),
   path("busca",views.course_search,name="busca")
]
