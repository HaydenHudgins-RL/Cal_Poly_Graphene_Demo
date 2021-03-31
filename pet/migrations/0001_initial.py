# Generated by Django 2.2.10 on 2021-03-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
