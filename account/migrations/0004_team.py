# Generated by Django 5.1.3 on 2024-11-27 09:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_company_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_lead', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='team_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
