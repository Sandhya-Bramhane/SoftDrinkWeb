# Generated by Django 5.0.3 on 2024-04-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DC', 'Coke'), ('RB', 'Red Bull'), ('VA', 'Vanilla'), ('CH', 'Cherry'), ('PS', 'Pepsi'), ('CO', 'Coca-Cola'), ('ZS', 'Zero'), ('BS', 'Bisleri'), ('EN', 'Energy'), ('DR', 'Dr-Pepper'), ('FA', 'Fanta'), ('MR', 'Monster'), ('SP', 'Sprite'), ('7U', '7UP'), ('LI', 'Lime'), ('NS', 'Nestlé')], max_length=2),
        ),
    ]
