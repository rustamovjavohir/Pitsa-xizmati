# Generated by Django 3.2.7 on 2022-02-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211004_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('KUTISHDA', 'Kutishda'), ('YOLDA', 'Yolda'), ('YETKAZIB_BERILDI', 'Yetkazib_berildi')], default='KUTISHDA', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(choices=[('KICHIK', 'Kichik'), ('ORTACHA', 'Ortacha'), ('KATTA', 'Katta'), ('JUDA_KATTA', 'Juda_Katta')], default='KICHIK', max_length=25),
        ),
    ]
