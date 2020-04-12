# Generated by Django 3.0.5 on 2020-04-11 21:09

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
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField()),
                ('action_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_user', to=settings.AUTH_USER_MODEL)),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='relationship',
            constraint=models.UniqueConstraint(fields=('user_one', 'user_two'), name='unique_users'),
        ),
    ]
