# Generated by Django 5.0.3 on 2024-06-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BS', 'Bisleri'), ('7U', '7UP'), ('RB', 'Red Bull'), ('FA', 'Fanta'), ('MR', 'Mirinda'), ('CO', 'Coca-Cola'), ('SP', 'Sprite'), ('MD', 'Mountain Dew'), ('DR', 'Dr-Pepper'), ('PS', 'Pepsi')], max_length=2),
        ),
    ]
