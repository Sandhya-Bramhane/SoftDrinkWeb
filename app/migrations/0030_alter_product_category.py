# Generated by Django 5.0.3 on 2024-04-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DR', 'Dr-Pepper'), ('PS', 'Pepsi'), ('CO', 'Coca-Cola'), ('SP', 'Sprite'), ('MR', 'Mirinda'), ('RB', 'Red Bull'), ('MD', 'Mountain Dew'), ('FA', 'Fanta'), ('7U', '7UP')], max_length=2),
        ),
    ]
