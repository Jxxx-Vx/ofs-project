# Generated by Django 3.0.14 on 2021-05-08 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0030_auto_20210508_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_app.Order'),
        ),
    ]
