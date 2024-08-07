# Generated by Django 5.0.7 on 2024-07-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_organizeevent_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizeevent',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('discarded', 'Discarded')], default='discarded', max_length=20),
            preserve_default=False,
        ),
    ]
