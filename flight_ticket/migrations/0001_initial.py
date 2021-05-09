# Generated by Django 3.1.8 on 2021-05-09 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('display_name', models.CharField(max_length=100)),
                ('color', models.CharField(default='#000000', max_length=7)),
                ('background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('default_value', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_category_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_category_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='LeadOrigin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('display_name', models.CharField(max_length=100)),
                ('color', models.CharField(default='#000000', max_length=7)),
                ('background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('default_value', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_leadorigin_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_leadorigin_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlightTicket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('reference', models.CharField(max_length=20)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('UN', 'Unplanned'), ('PL', 'Planned'), ('PO', 'Partially_organized'), ('OR', 'Organized'), ('PC', 'Partially_canceled'), ('PD', 'Partially_done'), ('CA', 'Canceled'), ('DO', 'Done')], default='UN', max_length=2)),
                ('reminder_date', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('customer_request', models.JSONField(blank=True, null=True)),
                ('gift_date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='flight_ticket.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_flightticket_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('lead_origin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='flight_ticket.leadorigin')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_flightticket_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
