# Generated by Django 2.0.3 on 2018-10-06 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gndu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gndu.Authors'),
            preserve_default=False,
        ),
    ]