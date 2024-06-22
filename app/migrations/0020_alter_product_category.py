# Generated by Django 5.0.3 on 2024-04-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FA', 'Fanta'), ('VA', 'Vanilla'), ('LI', 'Lime'), ('ZS', 'Zero'), ('CH', 'Cherry'), ('SP', 'Sprite'), ('DC', 'Coke'), ('EN', 'Energy')], max_length=2),
        ),
    ]
