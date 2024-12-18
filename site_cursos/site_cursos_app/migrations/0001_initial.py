# Generated by Django 5.1.4 on 2024-12-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=True)),
                ('ListaCursosInscritos', models.JSONField(blank=True, default=list)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
