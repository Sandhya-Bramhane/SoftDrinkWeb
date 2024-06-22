# Generated by Django 5.0.3 on 2024-03-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.TextField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('DC', 'Coke'), ('FA', 'Fanta'), ('ZS', 'Zero'), ('SP', 'Sprite'), ('LI', 'Lime'), ('VA', 'Vanilla'), ('CH', 'Cherry'), ('EN', 'Energy')], max_length=2)),
            ],
        ),
    ]
