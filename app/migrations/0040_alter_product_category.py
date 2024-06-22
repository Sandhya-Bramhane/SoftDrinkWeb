# Generated by Django 5.0.3 on 2024-05-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FA', 'Fanta'), ('BS', 'Bisleri'), ('DR', 'Dr-Pepper'), ('PS', 'Pepsi'), ('RB', 'Red Bull'), ('SP', 'Sprite'), ('MR', 'Mirinda'), ('MD', 'Mountain Dew'), ('7U', '7UP'), ('CO', 'Coca-Cola')], max_length=2),
        ),
    ]
