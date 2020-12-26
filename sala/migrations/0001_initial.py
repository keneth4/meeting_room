# Generated by Django 3.1.4 on 2020-12-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('libre', 'Libre'), ('ocupada', 'Ocupada')], default='libre', max_length=10)),
                ('horarios', models.TextField(blank=True)),
            ],
        ),
    ]
