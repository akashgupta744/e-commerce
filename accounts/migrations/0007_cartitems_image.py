# Generated by Django 5.0.2 on 2024-02-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_cartitems_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]