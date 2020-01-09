# Generated by Django 2.2.6 on 2019-10-26 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0002_auto_20191022_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lang', models.CharField(max_length=100)),
                ('verdict', models.IntegerField()),
                ('time', models.DecimalField(decimal_places=3, max_digits=5)),
                ('memory', models.IntegerField()),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
