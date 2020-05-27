# Generated by Django 3.0.2 on 2020-05-06 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drone', '0001_initial'),
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.TextField()),
                ('type_image', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.Drone')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Inspection')),
            ],
            options={
                'permissions': (('view_dashboard', 'Can view dashboard'),),
            },
        ),
    ]