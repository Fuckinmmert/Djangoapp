# Generated by Django 3.0.8 on 2020-07-19 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200719_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_Author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='articles.Article', verbose_name='Makale')),
            ],
        ),
    ]
