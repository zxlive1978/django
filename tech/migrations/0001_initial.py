# Generated by Django 2.2.9 on 2020-02-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='name_comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ins', models.CharField(max_length=100)),
                ('number', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('place', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('conf', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('msoffice', models.CharField(max_length=100)),
                ('buh', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('inwork', models.CharField(max_length=100)),
                ('decommissioned', models.CharField(max_length=100)),
                ('biosuser', models.CharField(max_length=100)),
                ('biossupper', models.CharField(max_length=100)),
                ('name', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='tech.name_comp')),
            ],
        ),
    ]
