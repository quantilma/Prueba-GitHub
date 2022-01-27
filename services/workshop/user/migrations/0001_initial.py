# Copyright 2020 Traceable, Inc.
#
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Generated by Django 2.2.13 on 2020-08-31 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField()),
                ('email', models.CharField(max_length=255, unique=True)),
                ('jwt_token', models.CharField(max_length=500, null=True, unique=True)),
                ('number', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.IntegerField(choices=[(2, 1), (0, 0)], default=0)),
            ],
            options={
                'db_table': 'user_login',
                'managed': False
            },
        ),
        migrations.CreateModel(
            name='VehicleCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vehicle_company',
                'managed': False
            },
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fuel_type', models.BigIntegerField()),
                ('model', models.CharField(max_length=255)),
                ('vehicle_img', models.CharField(max_length=255, null=True)),
                ('vehiclecompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.VehicleCompany'))
            ],
            options={
                'db_table': 'vehicle_model',
                'managed': False
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pincode', models.CharField(max_length=255, null=True)),
                ('vin', models.CharField(max_length=255)),
                ('year', models.BigIntegerField(null=True)),
                ('vehicle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.VehicleModel')),
                ('status', models.CharField(max_length=255)),
                ('location_id', models.BigIntegerField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'vehicle_details',
                'managed': False
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('available_credit', models.FloatField()),
                ('name', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'user_details',
                'managed': False
            },
        ),
    ]
