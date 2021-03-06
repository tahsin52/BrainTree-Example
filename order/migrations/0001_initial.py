# Generated by Django 3.2.7 on 2021-09-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('total_products', models.CharField(default=0, max_length=250)),
                ('total_amount', models.CharField(default=0, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(default=0, max_length=150)),
            ],
        ),
    ]
