# Generated by Django 5.0.3 on 2024-04-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_product_category_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LI', 'Lime'), ('CH', 'Cherry'), ('VA', 'Vanilla'), ('SP', 'Sprite'), ('EN', 'Energy'), ('ZS', 'Zero'), ('FA', 'Fanta'), ('DC', 'Coke')], max_length=2),
        ),
    ]
