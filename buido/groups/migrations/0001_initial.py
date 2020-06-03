# Generated by Django 3.0.6 on 2020-06-01 10:09

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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('creater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Affiliated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('attender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_affiliated', to=settings.AUTH_USER_MODEL)),
                ('group_attender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_affiliated', to='groups.Group')),
            ],
            options={
                'unique_together': {('attender', 'group_attender')},
                'index_together': {('attender', 'group_attender')},
            },
        ),
    ]
