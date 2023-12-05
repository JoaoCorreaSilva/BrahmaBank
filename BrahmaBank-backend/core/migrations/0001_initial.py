# Generated by Django 4.2.7 on 2023-12-02 17:17

import core.models
import core.utils.foto
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('registro', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=core.utils.foto.upload_user_photo)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('agencia', models.IntegerField()),
                ('tipo', models.CharField(choices=[['Corrente', 'Corrente'], ['Poupança', 'Poupança']], max_length=8)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('limite_cartao', models.DecimalField(decimal_places=2, max_digits=7)),
                ('usuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
            },
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conta')),
            ],
            options={
                'verbose_name': 'fatura',
                'verbose_name_plural': 'faturas',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantia', models.DecimalField(decimal_places=2, max_digits=7)),
                ('aprovado', models.BooleanField(default=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conta')),
            ],
            options={
                'verbose_name': 'emprestimo',
                'verbose_name_plural': 'emprestimos',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('validade', models.DateField()),
                ('bandeira', models.CharField(max_length=25)),
                ('cvv', models.CharField(max_length=25)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conta')),
            ],
            options={
                'verbose_name': 'cartão',
                'verbose_name_plural': 'cartões',
            },
        ),
    ]