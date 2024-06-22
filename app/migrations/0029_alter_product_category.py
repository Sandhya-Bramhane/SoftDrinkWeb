# Generated by Django 5.0.3 on 2024-04-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MD', 'Mountain Dew'), ('CO', 'Coca-Cola'), ('SP', 'Sprite'), ('7U', '7UP'), ('DR', 'Dr-Pepper'), ('MR', 'Mirinda'), ('PS', 'Pepsi'), ('FA', 'Fanta'), ('RB', 'Red Bull')], max_length=2),
        ),
    ]
