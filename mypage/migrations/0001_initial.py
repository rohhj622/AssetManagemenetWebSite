# Generated by Django 3.1 on 2020-10-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_id', models.CharField(max_length=12)),
                ('a_saving', models.IntegerField()),
                ('a_deposit', models.IntegerField()),
                ('a_stock', models.IntegerField()),
                ('a_fund', models.IntegerField()),
            ],
        ),
    ]
