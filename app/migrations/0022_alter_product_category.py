# Generated by Django 5.0.3 on 2024-04-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ZS', 'Zero'), ('DC', 'Coke'), ('EN', 'Energy'), ('LI', 'Lime'), ('VA', 'Vanilla'), ('FA', 'Fanta'), ('SP', 'Sprite'), ('CH', 'Cherry')], max_length=2),
        ),
    ]
