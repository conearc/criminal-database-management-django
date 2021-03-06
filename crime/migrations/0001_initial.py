# Generated by Django 3.0.3 on 2020-11-02 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('criminal', '0001_initial'),
        ('policeofficer', '0001_initial'),
        ('policestation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=4000)),
                ('firno', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('complainent_name', models.CharField(max_length=100)),
                ('complainent_address', models.CharField(max_length=500)),
                ('investigation_detail', models.CharField(max_length=4000)),
                ('criminals', models.ManyToManyField(related_name='criminal', related_query_name='crime', to='criminal.Criminal')),
                ('investigating_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policeofficer.PoliceOfficer')),
                ('policestation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policestation.PoliceStation')),
            ],
        ),
    ]
