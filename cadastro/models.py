from django.db import models
from django.db import models

class Alunos(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    renda = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    aluno = models.BooleanField(default=True)
    colaborador = models.BooleanField(default=False)
    arte1 = models.CharField(max_length=30, null=True, blank=True)
    arte2 = models.CharField(max_length=30, null=True, blank=True)
    arte3 = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='aluno_foto', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
