# Generated by Django 4.0 on 2021-12-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='arte1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='alunos',
            name='arte2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='alunos',
            name='arte3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='alunos',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='aluno_foto'),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='renda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
