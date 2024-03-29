# Generated by Django 4.2 on 2023-12-22 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_full_name', models.CharField(max_length=100)),
                ('payment_method', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card'), ('ET', 'Ethereum'), ('BC', 'Bitcoin')], default='CC', max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('successful', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
