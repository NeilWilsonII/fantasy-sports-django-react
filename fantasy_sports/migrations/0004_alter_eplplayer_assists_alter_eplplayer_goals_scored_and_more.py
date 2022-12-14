# Generated by Django 4.1 on 2022-09-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_sports', '0003_alter_eplplayer_points_per_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eplplayer',
            name='assists',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='goals_scored',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='now_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='points_per_game',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='selected_by_percent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='team',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eplplayer',
            name='total_points',
            field=models.IntegerField(null=True),
        ),
    ]
