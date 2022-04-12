# Generated by Django 4.0.1 on 2022-04-12 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0021_activemembers_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='medicinestockmodel',
            name='status',
            field=models.CharField(default='Usable', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='donation_date',
            field=models.DateField(default=datetime.date(2022, 4, 13)),
        ),
        migrations.AlterField(
            model_name='donationmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2022, 4, 13)),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='user_id',
            field=models.CharField(default=0, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicinestockmodel',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2022, 4, 13)),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='request_date',
            field=models.DateField(default=datetime.date(2022, 4, 13)),
        ),
    ]
