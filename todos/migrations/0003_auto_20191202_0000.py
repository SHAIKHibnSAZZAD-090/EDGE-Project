

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20191201_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
