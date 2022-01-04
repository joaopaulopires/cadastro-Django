from django.urls import path
from .views import lista_aluno
from .views import novo_aluno
from .views import update_aluno
from .views import delete_aluno
urlpatterns = [
   path('lista/', lista_aluno, name="lista_aluno"),
   path('novo', novo_aluno, name="novo_aluno"),
   path('update/<int:id>/', update_aluno, name="update_aluno"),
   path('delete/<int:id>/', delete_aluno, name="delete_aluno"),
]