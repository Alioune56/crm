# Generated by Django 5.2 on 2025-04-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.tag'),
        ),
    ]
