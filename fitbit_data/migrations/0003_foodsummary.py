# Generated by Django 3.1.1 on 2020-09-19 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitbit_auth', '0003_auto_20200917_1956'),
        ('fitbit_data', '0002_sleepsummary'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('data', models.JSONField(default=dict)),
                ('fb_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_summary', to='fitbit_auth.fitbituser')),
            ],
        ),
    ]
