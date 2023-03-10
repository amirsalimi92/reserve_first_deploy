# Generated by Django 4.1.5 on 2023-01-20 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FloorsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(choices=[(1, 'First floor'), (2, 'Second floor'), (3, 'Third floor')])),
                ('officeName', models.CharField(max_length=35)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Office.floorsdb')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.TextField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.customuser')),
            ],
        ),
    ]
