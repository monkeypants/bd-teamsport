# Generated by Django 2.1.7 on 2019-03-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_teamsport', '0003_auto_20190310_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='nickname',
            field=models.CharField(default='un-named opportunity', max_length=250),
            preserve_default=False,
        ),
    ]
