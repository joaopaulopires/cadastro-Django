#Documentação para Passwords no Django https://docs.djangoproject.com/pt-br/4.0/topics/auth/passwords/


from django.shortcuts import render, redirect, get_object_or_404
from .models import Alunos
from .form import AlunoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_aluno(request):
    alunos = Alunos.objects.all()
    print(alunos)
    return render(request, 'alunos.html', {'alunos': alunos})

@login_required
def novo_aluno(request):
    form = AlunoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_aluno')
    return render(request, 'aluno_form.html', {'form': form})

@login_required
def update_aluno(request, id):
    aluno = get_object_or_404(Alunos, pk=id)
    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('lista_aluno')
    return render(request, 'aluno_form.html', {'form': form})

@login_required
def delete_aluno(request, id):
    aluno = get_object_or_404(Alunos, pk=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_aluno')

    return render(request, 'delete_aluno_confirma.html', {'aluno': aluno})