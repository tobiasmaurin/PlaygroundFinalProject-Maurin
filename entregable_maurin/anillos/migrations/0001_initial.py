# Generated by Django 4.2.7 on 2023-12-05 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
                ('medida', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
