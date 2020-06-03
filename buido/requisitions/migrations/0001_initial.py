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
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField()),
                ('narration', models.CharField(max_length=250)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('is_requested', models.BooleanField(default=False)),
                ('annexe', models.FileField(blank=True, null=True, upload_to='attach/')),
                ('slug', models.SlugField(blank=True, max_length=130, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='req_group', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requisition', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequiDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narration', models.TextField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='requisitions.Requisition')),
            ],
        ),
    ]