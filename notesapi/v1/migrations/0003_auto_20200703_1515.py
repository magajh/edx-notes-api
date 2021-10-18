# Generated by Django 2.2.13 on 2020-07-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='quote',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='ranges',
            field=models.TextField(help_text='JSON, describes position of quote in the source text'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.TextField(default='[]', help_text='JSON, list of comma-separated tags'),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, default='', help_text="Student's thoughts on the quote"),
        ),
        migrations.AlterField(
            model_name='note',
            name='usage_id',
            field=models.CharField(help_text='ID of XBlock where the text comes from', max_length=255),
        ),
        migrations.AlterField(
            model_name='note',
            name='user_id',
            field=models.CharField(db_index=True, help_text='Anonymized user id, not course specific', max_length=255),
        ),
    ]