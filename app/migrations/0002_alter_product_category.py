# Generated by Django 5.0.3 on 2024-03-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DC', 'Coke'), ('FA', 'Fanta'), ('VA', 'Vanilla'), ('LI', 'Lime'), ('CH', 'Cherry'), ('SP', 'Sprite'), ('ZS', 'Zero'), ('EN', 'Energy')], max_length=2),
        ),
    ]
