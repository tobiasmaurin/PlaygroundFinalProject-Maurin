# Generated by Django 4.2.7 on 2023-12-31 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_usuario_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
