# Generated by Django 3.2.7 on 2021-09-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(verbose_name='ID пользователя в телеграме')),
                ('username', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Пользователь в телеграме',
                'verbose_name_plural': 'Пользователи в телеграме',
                'ordering': ['id'],
            },
        ),
    ]