# Generated by Django 4.1.5 on 2023-01-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('posteo', models.TextField()),
                ('fecha_posteo', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bloguers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('apellido', models.CharField(max_length=128)),
                ('nombre_usuario', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('hobbies', models.CharField(max_length=256)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]