# Generated by Django 4.2.2 on 2023-07-28 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_products_cart_user'),
        ('shop', '0004_product_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
