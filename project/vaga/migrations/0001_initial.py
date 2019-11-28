# Generated by Django 2.2.7 on 2019-11-28 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_vaga', models.CharField(max_length=255)),
                ('faixa_salarial', models.CharField(choices=[('Até 1.000', 'Até 1.000'), ('De 1.000 a 2.000', 'De 1.000 a 2.000'), ('De 2.000 a 3.000', 'De 2.000 a 3.000'), ('Acima de 3.000', 'Acima de 3.000')], max_length=100)),
                ('requisitos', models.TextField()),
                ('escolaridade_minima', models.CharField(choices=[('Ensino fundamental', 'Ensino fundamental'), ('Ensino médio', 'Ensino médio'), ('Tecnólogo', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('Pós / MBA / Mestrado', 'Pós / MBA / Mestrado'), ('Doutorado', 'Doutorado')], max_length=200)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
    ]
