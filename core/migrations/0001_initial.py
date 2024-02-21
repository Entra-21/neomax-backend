# Generated by Django 5.0.1 on 2024-02-21 13:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Insira o nome do exercício.', max_length=100, null=True)),
                ('gif', models.CharField(blank=True, help_text='Insira a URL do gif de demonstração do exercício.', max_length=100, null=True)),
                ('muscle_group', models.CharField(choices=[('Ombros', 'Ombros'), ('Peitoral', 'Peitoral'), ('Bíceps', 'Bíceps'), ('Antebraço', 'Antebraço'), ('Oblíquos', 'Oblíquos'), ('Abdômen', 'Abdômen'), ('Quadríceps', 'Quadríceps'), ('Abdutores', 'Abdutores'), ('Adutores', 'Adutores'), ('Trapézio', 'Trapézio'), ('Dorsais', 'Dorsais'), ('Lombar', 'Lombar'), ('Tríceps', 'Tríceps'), ('Glúteos', 'Glúteos'), ('Posteriores', 'Posteriores'), ('Panturrilha', 'Panturrilha')], help_text='Selecione o grupo muscular do exercício.', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, help_text='Insira a sua data de nascimento.', null=True)),
                ('profile_picture', models.CharField(blank=True, help_text='Insira a URL da imagem de perfil.', max_length=200, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Insira o nome da dieta.', max_length=50, null=True)),
                ('active', models.BooleanField(help_text='Informe se esta é a dieta ativa.')),
                ('user', models.ForeignKey(default=1, help_text='Informe o usuário de criação da dieta.', on_delete=django.db.models.deletion.CASCADE, related_name='diets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Insira o nome do dia.', max_length=50, null=True)),
                ('diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='core.diet')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Insira o nome da refeição.', max_length=100, null=True)),
                ('time', models.TimeField(blank=True, help_text='Insira o horário da refeição.', null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='core.day')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Insira o nome do treino.', max_length=50, null=True)),
                ('user', models.ForeignKey(default=1, help_text='Informe o usuário de criação do treino.', on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Insira o título da rotina.', max_length=50, null=True)),
                ('exercises', models.ManyToManyField(to='core.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='core.workout')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]