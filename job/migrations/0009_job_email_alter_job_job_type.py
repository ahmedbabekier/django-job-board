# Generated by Django 4.1.3 on 2023-03-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15),
        ),
    ]
