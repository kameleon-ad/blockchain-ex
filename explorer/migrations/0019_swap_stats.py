# Generated by Django 3.1.3 on 2020-12-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0018_max_privacy_withdraw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swap_stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc', models.CharField(max_length=16)),
                ('bch', models.CharField(max_length=16)),
                ('dash', models.CharField(max_length=16)),
                ('doge', models.CharField(max_length=16)),
                ('ltc', models.CharField(max_length=16)),
                ('qtum', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
