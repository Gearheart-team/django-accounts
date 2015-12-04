# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from ..models import user_image_upload_to
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('image', models.ImageField(null=True, upload_to=user_image_upload_to, blank=True)),
                ('preferred_name', models.CharField(max_length=30, blank=True)),
                ('gender', models.CharField(null=True, choices=[('f', 'Female'), ('m', 'Male')], max_length=1, blank=True, default=None)),
                ('birthdate', models.DateField(null=True, blank=True, verbose_name='Birth date')),
                ('phone', models.CharField(max_length=16, blank=True, verbose_name='Phone number')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('validated_at', models.DateTimeField(null=True, blank=True)),
                ('validation_key', models.UUIDField(null=True, default=uuid.uuid4, blank=True)),
                ('is_developer', models.BooleanField(default=False, help_text='User can see developer settings on the frontend clients.', verbose_name='Developer')),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', blank=True, related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
