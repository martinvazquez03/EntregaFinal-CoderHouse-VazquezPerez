# Generated by Django 4.2.7 on 2023-12-04 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='usuario',
            name='pais_origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cliente.pais'),
        ),
    ]
