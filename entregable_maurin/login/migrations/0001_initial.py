# Generated by Django 4.2.7 on 2023-12-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
