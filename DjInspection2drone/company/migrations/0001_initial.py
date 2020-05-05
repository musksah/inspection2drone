# Generated by Django 3.0.2 on 2020-05-05 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user_resgister', models.IntegerField(default=0)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
    ]
