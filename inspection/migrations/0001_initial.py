# Generated by Django 3.0.2 on 2020-05-06 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('pilot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreed_date', models.DateTimeField()),
                ('performed_date', models.DateTimeField()),
                ('state', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Realizada', 'Realizada')], max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user_resgister', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilot.Pilot')),
            ],
        ),
    ]