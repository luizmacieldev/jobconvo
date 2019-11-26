# Generated by Django 2.2.7 on 2019-11-26 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('vaga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Candidatado')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaga.Vaga')),
            ],
        ),
    ]
