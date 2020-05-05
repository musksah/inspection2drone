# Generated by Django 3.0.2 on 2020-05-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('birthdate', models.DateTimeField()),
                ('phonenumber', models.IntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user_resgister', models.IntegerField(default=0)),
            ],
        ),
    ]