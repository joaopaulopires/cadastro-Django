#Documentação para ModelForm https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/

from django.forms import ModelForm
from .models import Alunos

class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['first_name', 'last_name', 'age', 'renda', 'aluno', 'colaborador', 'arte1', 'arte2', 'arte3', 'bio', 'photo']