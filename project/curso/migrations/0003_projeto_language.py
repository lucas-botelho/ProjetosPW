# Generated by Django 5.0.4 on 2024-05-15 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_alter_disciplina_curriculariunitreadablecode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.linguagemdeprogramacao'),
        ),
    ]
