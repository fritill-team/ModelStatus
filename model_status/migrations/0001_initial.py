# Generated by Django 4.1.7 on 2023-03-12 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('pending', 'Pending'), ('published', 'Published'), ('archived', 'Archived'), ('suspended', 'Suspended'), ('canceled', 'Canceled'), ('rejected', 'Rejected'), ('approved', 'Approved'), ('started', 'Started'), ('ended', 'Ended')], default='draft', max_length=20)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_activity_log', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
    ]
