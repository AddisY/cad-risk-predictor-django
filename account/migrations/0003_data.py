# Generated by Django 2.1 on 2018-03-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_symptom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('trestbps', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chol', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thalach', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('ca', models.IntegerField()),
            ],
        ),
    ]
