# Generated by Django 3.0.6 on 2020-05-22 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_level', models.IntegerField(choices=[(1, 'Amateur'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Virtuoso')])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for_work', models.BooleanField(default=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('instruments', models.ManyToManyField(to='account.Instrument')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.Location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_filled', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Musician')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.Instrument')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.Location')),
            ],
        ),
    ]
