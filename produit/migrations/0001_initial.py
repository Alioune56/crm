# Generated by Django 5.2 on 2025-04-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prix', models.PositiveIntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
