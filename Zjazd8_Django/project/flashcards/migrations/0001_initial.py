# Generated by Django 5.0.3 on 2024-03-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlashcardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('question', models.TextField(max_length=1000)),
                ('answer', models.TextField(max_length=1000)),
            ],
        ),
    ]
