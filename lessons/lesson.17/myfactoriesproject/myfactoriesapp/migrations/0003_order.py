# Generated by Django 3.2.3 on 2021-05-31 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfactoriesapp', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('pending', 'Pending'), ('awaiting_shipment', 'Awaiting Shipment'), ('shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=30)),
                ('shipped_on', models.DateTimeField(null=True)),
                ('delivered_on', models.DateTimeField(null=True)),
                ('shipped_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myfactoriesapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
