# Generated by Django 3.1 on 2021-01-02 13:40

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, verbose_name='Username')),
                ('type', models.CharField(choices=[('W', 'Web'), ('T', 'Terminal')], default='W', max_length=2, verbose_name='Login type')),
                ('ip', models.GenericIPAddressField(verbose_name='Login ip')),
                ('city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('reason', models.SmallIntegerField(choices=[(0, '-'), (1, '用户名/密码 校验失败'), (2, 'MFA authentication failed'), (3, '用户名不存在'), (4, '密碼已過期')], default=0, verbose_name='Reason')),
                ('status', models.BooleanField(choices=[(True, '成功'), (False, '失敗')], default=True, max_length=2, verbose_name='Status')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date login')),
            ],
            options={
                'ordering': ['-datetime', 'username'],
            },
        ),
    ]
