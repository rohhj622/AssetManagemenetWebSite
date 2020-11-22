# Generated by Django 3.1 on 2020-11-14 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_id', models.CharField(max_length=12)),
                ('b_title', models.CharField(max_length=200)),
                ('b_text', models.TextField()),
                ('b_datetime', models.DateField(default=django.utils.timezone.now)),
                ('b_like', models.IntegerField(default=0)),
            ],
        ),
    ]