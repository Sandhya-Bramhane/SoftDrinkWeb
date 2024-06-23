# Generated by Django 5.0.3 on 2024-06-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MR', 'Mirinda'), ('CO', 'Coca-Cola'), ('FA', 'Fanta'), ('MD', 'Mountain Dew'), ('BS', 'Bisleri'), ('SP', 'Sprite'), ('DR', 'Dr-Pepper'), ('7U', '7UP'), ('RB', 'Red Bull'), ('PS', 'Pepsi')], max_length=2),
        ),
    ]
